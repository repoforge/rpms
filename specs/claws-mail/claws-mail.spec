# $Id:$
# Authority: hadams

Name:           claws-mail
Version:        3.1.0
Release:        1
Summary:        The extended version of Sylpheed
Group:          Applications/Internet
License:        GPL
URL:            http://claws-mail.org
Source0:        http://dl.sf.net/sylpheed-claws/%{name}-%{version}.tar.bz2
Source1:        claws-mail.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  flex, bison
BuildRequires:  glib2-devel >= 2.6.2
BuildRequires:  gtk2-devel >= 2.6.2
BuildRequires:  compface >= 1.4
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  openldap-devel >= 2.0.7
BuildRequires:  aspell-devel >= 0.50.1
BuildRequires:  pilot-link-devel
BuildRequires:  clamav-devel
BuildRequires:  bzip2-devel
BuildRequires:  gmp-devel
BuildRequires:  gnupg >= 1.2.1, gpgme-devel >= 1.0.1
BuildRequires:  desktop-file-utils startup-notification-devel
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  libetpan-devel >= 0.49
BuildRequires:  libgnomeprintui22-devel
BuildRequires:  compface-devel
BuildRequires:  perl
BuildRequires:  libtool
Obsoletes: sylpheed-claws <= 2.6.0
Provides: sylpheed-claws = %{version}-%{release}

%description
Claws Mail is an email client (and news reader), based on GTK+, featuring
quick response, graceful and sophisticated interface, easy configuration,
intuitive operation, abundant features, extensibility

%package        devel
Summary:        Development package for %{name}
Group:          Development/Libraries
Obsoletes:      sylpheed-claws-devel <= 2.6.0
Provides:       sylpheed-claws-devel = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains the header files  and pkgconfig file needed
for development with %{name}.

%package plugins-clamav
Summary:        Clamav antivirus plugin for claws-mail
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-clamav <= 2.6.0
Provides:       sylpheed-claws-plugins-clamav = %{version}-%{release}

%description plugins-clamav
%{summary}

%package plugins-dillo
Summary:        Dillo HTML viewer plugin for claws-mail
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}
Requires:       dillo
Obsoletes:      sylpheed-claws-plugins-dillo <= 2.6.0
Provides:       sylpheed-claws-plugins-dillo = %{version}-%{release}

%description plugins-dillo
%{summary}

%package plugins-spamassassin
Summary:        Spamassassin plugin for claws-mail
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}
Requires:       spamassassin
Obsoletes:      sylpheed-claws-plugins-spamassassin <= 2.6.0
Provides:       sylpheed-claws-plugins-spamassassin = %{version}-%{release}

%description plugins-spamassassin
%{summary}

%package plugins-pgp
Summary:        PGP plugin for signing and encrypting mail
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-pgp <= 2.6.0
Provides:       sylpheed-claws-plugins-pgp = %{version}-%{release}

%description plugins-pgp
%{summary}

%package plugins-bogofilter
Summary:        Bogofilter plugin for claws-mail
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-bogofilter <= 2.6.0
Provides:       sylpheed-claws-plugins-bogofilter = %{version}-%{release}

%description plugins-bogofilter
%{summary}

%prep
%setup -q

%build
%configure --enable-openssl --enable-ipv6 \
           --enable-ldap --enable-jpilot \
           --enable-spamassassin-plugin \
           --enable-aspell \
           --disable-dependency-tracking \
           --disable-rpath \
           --enable-compface

%{__make} %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool

%{__make} check


%install
%{__rm} -rf ${RPM_BUILD_ROOT}
export LIBTOOL=%{_bindir}/false
%makeinstall gnomedatadir=${RPM_BUILD_ROOT}/%{_datadir}

%find_lang claws-mail

desktop-file-install \
        --vendor=fedora \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
        --add-category=X-Fedora \
	%{SOURCE1}

%{__rm} -f ${RPM_BUILD_ROOT}%{_infodir}/dir
%{__rm} -rf ${RPM_BUILD_ROOT}%{_datadir}/gnome

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT}/%{_libdir}/claws-mail/plugins/ -type f -name \
"*.a" -exec rm -f {} ';'

%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps

%{__install} %{_builddir}/%{name}-%{version}/claws-mail.png \
${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

# we include the manual in the doc section
%{__rm} -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/claws-mail

# we have an desktop file already (#223436)
%{__rm} -rf ${RPM_BUILD_ROOT}%{_datadir}/applications/claws-mail.desktop

# Makefiles don't need to be in doc
find manual -type f -name Makefile.am -exec rm {} \;
find manual -type f -name Makefile.in -exec rm {} \;
find manual -type f -name Makefile -exec rm {} \;

# fix pkconfig
%{__perl} -i  -pe 's/\/local//g;' ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/claws-mail.pc

# don't think we need icon-theme.cache
%{__rm} -f ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/icon-theme.cache

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files -f claws-mail.lang
%defattr(-,root,root,0755)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING
%doc NEWS README
%doc TODO
%doc manual/*
%{_bindir}/*
%dir %{_libdir}/claws-mail/
%dir %{_libdir}/claws-mail/plugins/
%{_libdir}/claws-mail/plugins/trayicon.so
%{_datadir}/pixmaps/*
#%{_datadir}/claws-mail
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%files devel
%defattr(-,root,root,0755)
%{_includedir}/claws-mail/
%{_libdir}/pkgconfig/claws-mail.pc
%{_libdir}/claws-mail/plugins/*deps

%files plugins-clamav
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/clamav_plugin.so

%files plugins-dillo
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/dillo_viewer.so

%files plugins-spamassassin
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/spamassassin.so

%files plugins-pgp
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/pgp*.so

%files plugins-bogofilter
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/bogofilter.so


%changelog
* Wed Nov 21 2007 Heiko Adams <info@fedora-blog.de> 
3.1.0
- version upgrade

* Thu Oct 02 2007 Heiko Adams <info@fedora-blog.de> 
3.0.2
- version upgrade

* Wed Sep 19 2007 Heiko Adams <info@fedora-blog.de> 
3.0.1
- version upgrade

* Wed Sep 05 2007 Heiko Adams <info@fedora-blog.de> 
3.0.0
- version upgrade

* Sun Aug 12 2007 Heiko Adams <info@fedora-blog.de>
2.10.0-1
- version upgrade
- rebuild for rpmforge

* Sat Apr 21 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9.1-1
- version upgrade which fixes CVE-2007-1558 (see #237293)

* Mon Apr 16 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9.0-1
- version upgrade (should resolve #232675)
- fix BR

* Tue Mar 06 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.8.1-1
- version upgrade

* Tue Feb 27 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.8.0-1
- version upgrade
- fix #228160
- devel subpackage does not require claws-mail anymore
- fix rpath issues
- fix pkg-config file

* Wed Feb 07 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.7.2-1
- version upgrade
- fix #223436
- another try on #221708

* Wed Jan 17 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.7.1-1
- version upgrade #222279
- fix xface support #221708

* Thu Jan 11 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.7.0-1
- version upgrade

* Fri Dec 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.1-2
- fix Obsoletes/Requires

* Mon Dec 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.1-1
- version upgrade
- package is now named claws-mail instead of sylpheed-claws
- fix #218190, #218187

* Mon Nov 06 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.0-1
- version upgrade

* Thu Oct 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.6-1
- version upgrade

* Thu Oct 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.5-1
- version upgrade

* Sat Oct 07 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.3-1
- version upgrade

* Wed Sep 27 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-1
- version upgrade

* Tue Sep 26 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.1-1
- version upgrade
- should fix (#204340)

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.4.0-2
- FE6 rebuild

* Mon Jul 31 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.4.0-1
- version upgrade

* Mon Jun 26 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.3.1-1
- version upgrade

* Mon Jun 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.3.0-1
- version upgrade

* Fri Jun 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.2.3-1
- version upgrade

* Mon Jun 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.2.1-1
- version upgrade

* Mon May 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.2.0-1
- version upgrade

* Sat Apr 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.1.1-1
- split plugins from main package to ease requirements (#189113)
- version upgrade (#183357)
- fix libpisock (#189585)

* Wed Apr 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.1.0-1
- version upgrade

* Fri Mar 31 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-4
- #187383: add BR libgnomeprintui22-devel

* Thu Mar 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-3
- Fix .desktop 

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-2
- Rebuild for Fedora Extras 5

* Fri Feb 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-1
- version upgrade
- fix summary

* Wed Jan 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-0.rc4
- version upgrade

* Mon Jan 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-0.rc3
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-0.rc2
- version upgrade

* Sun Dec 04 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-0.rc1
- version upgrade

* Mon Nov 21 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.100-2
- drop program suffix (causes sylpheed-claws-claws bin)

* Thu Nov 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.100-1
- version upgrade

* Sat Oct 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.15-1
- version upgrade

* Fri Sep 09 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.14-1
- version upgrade

* Mon Aug 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-4
- fix files

* Mon Aug 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-3
- add gmp-devel BR

* Mon Aug 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-2
- add bzip2-devel BR

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-1
- upgrade
- switch s/gpgme03/gpgme/
- need libetpan

* Thu Jul 07 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.12-2
- add some doc
- fix pixmap installation

* Wed Jul 06 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.12-1
- version upgrade
- add dist tag

* Thu May 26 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.11-1
- change to gtk2 version

* Thu Apr 14 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.4-2
- minor cleanups
- remove aspell version check

* Thu Mar 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.4-1
- Version upgrade

* Wed Mar 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.3-1
- Version upgrade

* Fri Mar 18 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.1-3
- Don't include static libs in plugin directory.
- Set --with-gpgme-prefix to use relocated gpgme03 package contents.
- BR startup-notification-devel

* Sat Mar 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.1-2
- fixed some sylpheed/sylpheed-claws
- removed Conflictes sylpheed

* Wed Feb 09 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:1.0.1-1
- version upgrade
- cleaned up BuildRequires/Requires and configure options

* Tue Dec 21 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.13-1
- version upgrade
- remove old configure options for GnuPG support (moved to a new plugin now)
- enable new pgpmime-plugin

* Tue Jul 20 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.12-1
- version upgrade
- lots of s/sylpheed/sylpheed-claws/

* Mon May 31 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.11-0.fdr.1
- version upgrade

* Tue Mar 09 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.10-0.fdr.1
- new upstream version

* Fri Feb 13 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.9-0.fdr.1
- version upgrade
* Thu Jan 01 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.8-0.fdr.1
- version upgrade

* Thu Dec 18 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.7-0.fdr.2
- added missing defattr to devel rpm (fixes pending issue)

* Thu Nov 27 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.7-0.fdr.1
- version upgrade

* Wed Oct 08 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.6-0.fdr.8
- version upgrade

* Tue Sep 16 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.5-0.fdr.7
- minor fixes (see #545 #2{1,2})

* Mon Sep 15 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.5-0.fdr.6
- added specfile changes provided by Michael Schwendt
- made aspell-devel conditional severn only

* Fri Sep 12 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.5-0.fdr.5
- version upgrade (thus devel package)
- readded aspell-devel (still only works for > severn but 'a nice to have')

* Sat Aug 30 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.4-0.fdr.4
- reintroduced --enable-aspell without BuildRequires so that it will work in
  severn and just be ignored on > shrike
- changed openssl cflags (now via pkg-config)

* Wed Aug 06 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.4-0.fdr.3
- upgrade to new version
- no aspell support till version >= 0.5.0 is aviable

* Sat Aug 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.3-0.fdr.2
- Added BuildRequires openldap-devel, pilot-link-devel
- Excluded static archives
- Changed desktop file

* Fri Aug 01 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.9.3-0.fdr.1
- Initial RPM release.
