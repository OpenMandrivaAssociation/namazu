# XXX is this right - it was /var/lib before FHS macros
%define _localstatedir	/var/lib
%define _libexecdir	/var/www/cgi-bin
%define libname %mklibname %name 3

Summary: Full-text search engine
Name: namazu
Version: 2.0.20
Release: 2
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
Source0: http://www.namazu.org/stable/%{name}-%{version}.tar.gz
URL: http://www.namazu.org/

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
Provides: lib%{name}-devel = %{EVRD}
Provides: %{name}-devel = %{EVRD}


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
%makeinstall

mv %{buildroot}%{_sysconfdir}/namazu/namazurc-sample \
	%{buildroot}%{_sysconfdir}/namazu/namazurc
mv %{buildroot}%{_sysconfdir}/namazu/mknmzrc-sample \
	%{buildroot}%{_sysconfdir}/namazu/mknmzrc
chmod a+rw -R %{buildroot}%{_localstatedir}/namazu
chmod a+rw -R %{buildroot}%{_localstatedir}/namazu/index

rm -f  %{buildroot}/%{_datadir}/locale/ja_JP.SJIS/LC_MESSAGES/namazu.mo
%find_lang %{name}

%files -f %{name}.lang
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
%{_libdir}/libnmz.so.7*

%files -n %{libname}-devel
%{_bindir}/nmz-config
%{_includedir}/namazu/*.h
%{_libdir}/libnmz.so
%{_libdir}/libnmz.a

%files cgi
%{_libexecdir}/namazu.cgi




%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.0.20-1mdv2011.0
+ Revision: 645329
- update to new version 2.0.20

* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.19-2mdv2011.0
+ Revision: 620474
- the mass rebuild of 2010.0 packages

* Sun Jun 21 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0.19-1mdv2010.0
+ Revision: 387855
- update to new version 2.0.19
- fix files section
- use autoreconf and re-enable libtoolize
- fix license tag

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.0.14-4mdv2009.0
+ Revision: 253565
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.14-2mdv2008.1
+ Revision: 170993
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.0.14-1mdv2008.1
+ Revision: 130474
- kill re-definition of %%buildroot on Pixel's request
- fix man pages


* Mon Jul 25 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.0.14-1mdk
- New release 2.0.14

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.13-1mdk
- 2.0.13

* Sat Nov 15 2003 Michael Scherer <scherer.michael@free.fr> 2.0.12-2mdk 
- split library
- fix changelog ( replace %% by %% )
- variuous rpmlint fix

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.0.12-1mdk
- 2.0.12

* Fri Jan 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0.10-1mdk
- 2.0.10

* Fri Nov 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0.9-1mdk
- 2.0.9

* Tue Nov 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0.8-1mdk
- 2.0.8

* Fri Sep 14 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 2.0.7-1mdk
- first mandrake release
- added BuildRequires perl-File-MMagic

* Tue Sep 11 2001 Ryuji Abe <rug@namazu.org> 2.0.6-2
- fix newgettext patch.

* Mon Aug 13 2001 Ryuji Abe <rug@namazu.org> 2.0.6-1
- update to 2.0.6

* Thu Jul 26 2001 Ryuji Abe <rug@namazu.org>
- fix %%files

* Sat Jun 23 2001 Ryuji Abe <rug@namazu.org>
- fix summary and %%description

* Thu May 31 2001 Ryuji Abe <rug@namazu.org>
- fix %%files
- fix again cgi-bin location to /var/www/cgi-bin

* Mon May 28 2001 Ryuji Abe <rug@namazu.org>
- clean up spec file
- more macros
- provide cgi package
- fix cgi-bin location /home/httpd/cgi-bin to /var/www/namazu-cgi-bin

* Wed Mar 21 2001 Ryuji Abe <rug@namazu.org>
- Rebuilt for 7.1 beta
- more macros
- fix dependencies
- exclude unnecessary ja_JP.SJIS catalog.

* Thu Oct 26 2000 Ryuji Abe <rug@namazu.org>
- Requires perl-File-MMagic >= 1.09.
- Add BuildRequires.

* Tue Aug 22 2000 Ryuji Abe <rug@namazu.org>
- Fixed %%localstatedir /var to /var/lib.

* Tue Apr 25 2000 Ryuji Abe <rug@namazu.org>
- Ignore %%{prefix}/share/namazu/etc.

* Sun Feb 20 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- Install namazu.cgi at /home/httpd/cgi-bin.
- Fixed typo.

* Sat Feb 19 2000 Satoru Takabayashi <satoru-t@is.aist-nara.ac.jp>
- Change URL.

* Tue Feb 15 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- Delete package entries elisp and cgi.

* Wed Feb 02 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- Adapted for namazu-current.
- Changed group Utilities/Text -> Applications/Text.

* Thu Dec 30 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- rpm-3.0.x adaptations.
- Added package entries elisp and cgi (currently comment out). 
  [Merged SAKA Toshihide's changes for Kondara MNU/Linux.]

* Mon Nov 08 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Changed includedir %%{prefix}/include/namazu.
- Bug fix at configure section.

* Thu Nov 04 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Added nmz-config in devel package.

* Wed Nov 03 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Use our definite macros, ver, rel, prefix, sysconfdir, and localstatedir.
- If configure not found, use autogen.sh.
- Optimized for SMP environment.
- Build devel package.

* Tue Oct 12 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Fixed correctly executables entry at %%files.
- Added missing /usr/share/locale entry at %%files.

* Thu Aug 26 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Requires perl >= 5.004.
- Delete Packager tag.
- Clean up at %%prep.
- Use CFLAGS="$RPM_OPT_FLAGS" at %%build.
- Use $RPM_BUILD_ROOT variables at %%install.
- Change configure option at %%build and %%files for new namazu directory structure.

* Sun May 23 1999 Taku Kudoh <taku@TAHOO.ORG>
-

