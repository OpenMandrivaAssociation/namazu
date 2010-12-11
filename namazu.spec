# XXX is this right - it was /var/lib before FHS macros
%define _localstatedir	/var/lib
%define _libexecdir	/var/www/cgi-bin
%define version   2.0.19
%define name      namazu
%define release   %mkrel 2
%define libname %mklibname %name 3

Summary: Full-text search engine
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: File tools
BuildRequires: perl >= 5.6.0
BuildRequires: perl-NKF >= 1.70
BuildRequires: perl-Text-Kakasi >= 1.00
BuildRequires: perl-File-MMagic >= 1.12
Requires: perl-File-MMagic >= 1.12
Requires:  perl-NKF >= 1.70
Requires: kakasi >= 2.3.0
Requires: perl-Text-Kakasi >= 1.00
Source: http://www.namazu.org/stable/%{name}-%{version}.tar.gz
URL: http://www.namazu.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Namazu is a full-text search engine software intended for easy use.
Not only it works as CGI program for small or medium scale WWW
search engine, but also works as personal use such as search system
for local HDD.

%package -n %{libname}
Summary: Libraries of Namazu
Group: Development/C
Requires: %{libname} = %{version}

%description -n %{libname}
Libraries used by Namazu.


%package  -n %{libname}-devel
Summary: Libraries and include files of Namazu
Group: Development/C
Requires: %{libname} = %{version}
Provides: lib%{name}-devel
Provides: %{name}-devel

Obsoletes: %{name}-devel


%description -n %{libname}-devel
Libraries and include files of Namazu.

%package cgi
Summary: CGI interface for Namazu
Group: Networking/WWW
Requires: %{name} = %{version}
Requires: webserver

%description cgi
A CGI interface for Namazu.


%prep 
%setup -q

%build
autoreconf -f -i
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall

mv %{buildroot}%{_sysconfdir}/namazu/namazurc-sample \
	%{buildroot}%{_sysconfdir}/namazu/namazurc
mv %{buildroot}%{_sysconfdir}/namazu/mknmzrc-sample \
	%{buildroot}%{_sysconfdir}/namazu/mknmzrc
chmod a+rw -R %{buildroot}%{_localstatedir}/namazu
chmod a+rw -R %{buildroot}%{_localstatedir}/namazu/index

rm -f  %{buildroot}/%{_datadir}/locale/ja_JP.SJIS/LC_MESSAGES/namazu.mo
%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun  -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog ChangeLog.1 CREDITS COPYING HACKING HACKING-ja
%doc INSTALL INSTALL-ja README README-es README-ja NEWS THANKS TODO
%doc etc/namazu.png
%config(noreplace) %{_sysconfdir}/namazu/*
%{_bindir}/namazu
%{_bindir}/bnamazu
%{_bindir}/*nmz
%{_bindir}/mailutime
%{_bindir}/nmzgrep
%{_bindir}/nmzegrep
%{_bindir}/nmzmerge
%{_bindir}/nmzcat
%{_mandir}/man1/namazu.*
%{_mandir}/man1/mknmz.*
%{_datadir}/namazu/doc/*
%{_datadir}/namazu/filter/*
%{_datadir}/namazu/pl/*
%{_datadir}/namazu/template/*
%{_datadir}/namazu/etc/
%dir %{_localstatedir}/namazu
%dir %{_localstatedir}/namazu/index

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/libnmz.so.7*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_bindir}/nmz-config
%{_includedir}/namazu/*.h
%{_libdir}/libnmz.so
%{_libdir}/libnmz.a
%{_libdir}/libnmz.la

%files cgi
%defattr(-, root, root)
%{_libexecdir}/namazu.cgi


