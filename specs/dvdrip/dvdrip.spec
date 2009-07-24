# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_sitelib %(eval "`perl -V:installsitelib`"; echo $installsitelib)

%define desktop_vendor rpmforge

Summary: Graphical DVD ripping and encoding tool based on transcode
Name: dvdrip
Version: 0.98.10
Release: 1
License: GPL+ or Artistic
Group: Applications/Multimedia
URL: http://www.exit1.org/dvdrip/

Source: http://www.exit1.org/dvdrip/dist/dvdrip-%{version}.tar.gz
Patch0: Video-DVDRip-0.97.8-nontplworkaround.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: perl(Event::ExecFlow) >= 0.62
BuildRequires: perl(Event::RPC)
BuildRequires: perl(Gtk2) >= 1.081
BuildRequires: perl(Gtk2::Ex::FormFactory) >= 0.65
BuildRequires: perl(Locale::TextDomain) >= 1.16
Requires: ImageMagick
Requires: lsdvd
Requires: ogmtools
Requires: perl(Event::ExecFlow) >= 0.62
Requires: perl(Gtk2) >= 1.081
Requires: perl(Gtk2::Ex::FormFactory) >= 0.65
Requires: perl(Locale::TextDomain) >= 1.16
Requires: subtitleripper
Requires: transcode >= 0.6.13
Requires: vcdimager

Obsoletes: perl-Video-DVDRip <= %{version}-%{release}
Provides: perl-Video-DVDRip = %{version}-%{release}

%description
dvd::rip is a full featured DVD copy program. It provides an easy to use but
feature-rich Gtk+ GUI to control almost all aspects of the ripping and
transcoding process. It uses the widely known video processing swissknife
transcode and many other Open Source tools.


%prep
%setup
%patch0 -p1 -b .nontplworkaround

# Desktop entry
%{__cat} <<EOF >dvdrip.desktop
[Desktop Entry]
Name=DVD Ripper and Encoder
Comment=Backup and compression utility for DVDs
Exec=dvdrip
Icon=%{perl_sitelib}/Video/DVDRip/icon.xpm
Terminal=false
Type=Application
Categories=AudioVideo;
EOF

%build
%{__perl} Makefile.PL
# Disable %{?_smp_mflags}, it makes build fail (0.98.0)
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
    INSTALLSCRIPT="%{buildroot}%{_bindir}" \
    INSTALLSITELIB="%{buildroot}%{perl_sitelib}" \
    INSTALLSITEARCH="%{buildroot}%{perl_sitearch}" \
    INSTALLMAN1DIR="%{buildroot}%{_mandir}/man1" \
    INSTALLSITEMAN1DIR="%{buildroot}%{_mandir}/man1" \
    INST_MAN1DIR="%{buildroot}%{_mandir}/man1" \
    INSTALLMAN3DIR="%{buildroot}%{_mandir}/man3" \
    INSTALLSITEMAN3DIR="%{buildroot}%{_mandir}/man3" \
    INST_MAN3DIR="%{buildroot}%{_mandir}/man3"

# Unpackaged strange files!
%{__rm} -f %{buildroot}%{_mandir}/man?/.exists* || :

# Unneeded, all is in sitelib (only a .packlist in there)
%{__rm} -rf %{buildroot}%{perl_sitearch}

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    dvdrip.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYRIGHT Credits README TODO
%doc %{_mandir}/man*/*
%attr(0755, root, root) %{_bindir}/*
%lang(cs) %{perl_sitelib}/LocaleData/cs/LC_MESSAGES/video.dvdrip.mo
%lang(da) %{perl_sitelib}/LocaleData/da/LC_MESSAGES/video.dvdrip.mo
%lang(de) %{perl_sitelib}/LocaleData/de/LC_MESSAGES/video.dvdrip.mo
%lang(es) %{perl_sitelib}/LocaleData/es/LC_MESSAGES/video.dvdrip.mo
%lang(fr) %{perl_sitelib}/LocaleData/fr/LC_MESSAGES/video.dvdrip.mo
%lang(it) %{perl_sitelib}/LocaleData/it/LC_MESSAGES/video.dvdrip.mo
%lang(sr) %{perl_sitelib}/LocaleData/sr*/LC_MESSAGES/video.dvdrip.mo
%{perl_sitelib}/Video/
%{_datadir}/applications/%{desktop_vendor}-dvdrip.desktop

%changelog
* Fri Jul 24 2009 Dag Wieers <dag@wieers.com> - 0.98.10-1
- Updated to release 0.98.10.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 0.98.7-1
- Update to 0.98.7.

* Mon Apr 16 2007 Matthias Saou <http://freshrpms.net/> 0.98.6-1
- Update to 0.98.6.

* Mon Apr  2 2007 Matthias Saou <http://freshrpms.net/> 0.98.4-2
- Include two fixes from Jörn.

* Mon Mar 26 2007 Matthias Saou <http://freshrpms.net/> 0.98.4-1
- Update to 0.98.4.

* Mon Mar 12 2007 Matthias Saou <http://freshrpms.net/> 0.98.3-1
- Update to 0.98.3.

* Mon Nov 27 2006 Matthias Saou <http://freshrpms.net/> 0.98.2-1
- Update to 0.98.2.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.98.1-1
- Rename to dvdrip, like upstream did.
- Obsolete up to last know version of perl-Video-DVDRip (<= 0.98.1-2).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.98.1-1
- Update to 0.98.1.

* Tue Aug 22 2006 Matthias Saou <http://freshrpms.net/> 0.98.0-1
- Update to 0.98.0.
- Upstream changed the tarball name to "dvdrip" now, the package will probably
  change soon. Provide dvdrip with same V-R for now.
- Add perl(Event::RPC) build requirement, otherwise the bundled gets installed.
- Update source URL and description.

* Sun Jul  2 2006 Matthias Saou <http://freshrpms.net/> 0.97.12-1
- Update to 0.97.12.
- Remove no longer needed tet patch, since we use the "fixed" source.
- Now require Gtk2::Ex::FormFactory >= 0.65.

* Tue Jun 20 2006 Matthias Saou <http://freshrpms.net/> 0.97.11-2
- Exclude experimental dvdrip-tet binary, since it also had a leftover
  reference to FixLocaleTextDomainUTF8 that broke the automatically
  generated dependencies.

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.97.11-1
- Update to 0.97.11.

* Tue Apr 25 2006 Matthias Saou <http://freshrpms.net/> 0.97.10-1
- Update to 0.97.10.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.97.8-1
- Update to 0.97.8.
- Update NPTL workaround disabling patch.
- Require Gtk2-Ex-FormFactory >= 0.62.
- Fix Source URL to point to valid location (was missing "/pre").

* Thu Mar 23 2006 Matthias Saou <http://freshrpms.net/> 0.97.6-3
- Add patch to default to NPTL workaround disabled, since it's causing dvd::rip
  to not work properly on FC5.
- Add lsdvd requirement, since it's used for faster DVD TOC reading.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.97.6-2
- Remove _smp_mflags as it makes the build fail.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.97.6-1
- Update to gtk2 branch at last, 0.97.6.
- Include doc.
- Re-enable auto-requires, so perl(Event) is now required.

* Sun Jul 31 2005 Matthias Saou <http://freshrpms.net/> 0.52.6-1
- Update to 0.52.6.

* Mon May 23 2005 Matthias Saou <http://freshrpms.net/> 0.52.5-1
- Update to 0.52.5.

* Tue May 17 2005 Matthias Saou <http://freshrpms.net/> 0.52.4-1
- Update to 0.52.4.

* Mon Mar 14 2005 Matthias Saou <http://freshrpms.net/> 0.52.3-1
- Update to 0.52.3.

* Sun Jan  9 2005 Matthias Saou <http://freshrpms.net/> 0.52.2-1
- Update to 0.52.2.

* Tue Jan  4 2005 Matthias Saou <http://freshrpms.net/> 0.52.0-1
- Update to 0.52.0.

* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 0.51.4-0
- Update to 0.51.4.

* Sun Dec 12 2004 Matthias Saou <http://freshrpms.net/> 0.51.3-0
- Update to 0.51.3.

* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 0.51.2-0
- Update to unstable 0.51.2, as it adds compatibility for transcode 0.6.13.
- Added translations that are now included and perl(Locale::Messages) dep.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 0.50.18-3
- Changed LD_ASSUME_KERNEL to 2.4.1 for x86_64.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.50.18-2
- Rebuild for Fedora Core 2.

* Mon Apr 19 2004 Matthias Saou <http://freshrpms.net/> 0.50.18-1
- Update to 0.50.18.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 0.50.17-1
- Update to 0.50.17.

* Sat Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.50.16-3
- Changed the LD_ASSUME_KERNEL from 2.4.19 to 2.2.5 to actually work!

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.50.16-2
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 0.50.16-1
- Update to 0.50.16.

* Mon Aug 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.15.

* Sun Jun 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.14.

* Sun May 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.13.

* Sat Apr 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.11.

* Wed Apr  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.10.
- Fix the automatic dep problem.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sat Mar 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.9.

* Fri Mar  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.8.

* Tue Mar  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.7, boy this is going fast! :-)

* Mon Mar  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.5.
- Update to 0.50.6.

* Mon Feb 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.4.

* Tue Feb 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.3.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.2.

* Mon Feb 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.50.0.

* Tue Jan  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.48.8.

* Fri Dec 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.48.6.
- Added menu entry.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.48.5.

* Mon Nov 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.48.0.
- At last, rebuilt for Red Hat Linux 8.0.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.46.

* Thu Aug  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.44.
- Added build dependency on Gtk-Perl.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Sun Jun 16 2002 Nemo <no@one>
- v0.43

* Sun Jun 09 2002 Nemo <no@one>
- v0.42

* Tue May 14 2002 Nemo <no@one>
- v0.40

* Mon May 13 2002 Nemo <no@one>
- v0.39-2
- Michel Alexandre Salim <salimma1@yahoo.co.uk> suggested an improvement in the PATH used by "make test"

* Tue Mar 05 2002 Nemo <no@one>
- bumped up to v0.34

* Tue Feb 19 2002 Nemo <no@one>
- bumped up to v0.33

* Mon Feb 18 2002 Nemo <no@one>
- bumped up to v0.31

* Sun Jan 20 2002 Nemo <no@one>
- bumped up to v0.30

* Sat Jan 19 2002 Nemo <no@one>
- bumped up to v0.29

* Sun Jan 06 2002 Nemo <no@one>
- bumped up to v0.28

* Sat Dec 15 2001 Nemo <no@one>
- First version, v0.25

