# $Id$
# Authority: dag
# Upstream: Jörn Reder <joern$zyn,de>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define desktop_vendor  rpmforge

%define real_name Video-DVDRip

Summary: Graphical DVD ripping tool based on transcode
Name: perl-Video-DVDRip
Version: 0.52.6
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://www.exit1.org/dvdrip/
#URL: http://search.cpan.org/dist/Video-DVDRip/

Source: http://www.exit1.org/dvdrip/dist/Video-DVDRip-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Video/dvdrip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: Gtk-Perl
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: transcode >= 0.6.13
Requires: Gtk-Perl, ImageMagick, ogmtools, subtitleripper, vcdimager
Requires: perl(Locale::Messages)

Provides: dvdrip = %{version}-%{release}
Obsoletes: dvdrip <= %{version}-%{release}

#AutoReq: no

%description
dvd::rip is a Perl Gtk+ based DVD copy program built on top of a low level
DVD Ripping API, which uses the Linux Video Stream Processing Tool transcode.

%prep
%setup -n %{real_name}-%{version}

%{__cat} > dvdrip.desktop <<EOF
[Desktop Entry]
Name=DVD Ripper and Encoder
Comment=Backup and compression utility for DVDs
Exec=dvdrip
Icon=%{perl_sitelib}/Video/DVDRip/icon.xpm
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 dvdrip.desktop %{buildroot}%{_sysconfdir}/X11/applnk/Multimedia/dvdrip.desktop
%else
    %{__mkdir_p} %{buildroot}%{_datadir}/applications
    desktop-file-install --vendor %{desktop_vendor} \
        --dir %{buildroot}%{_datadir}/applications \
        dvdrip.desktop
%endif

# Unpackaged strange files!
%{__rm} -f %{buildroot}%{_mandir}/man?/.exists* || :

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes* COPYRIGHT Credits MANIFEST META.yml README TODO
%doc %{_mandir}/man1/dr_progress.1*
%doc %{_mandir}/man1/dr_splitpipe.1*
%doc %{_mandir}/man1/dvdrip.1*
%doc %{_mandir}/man3/*.3pm*
%lang(cs) %{perl_vendorlib}/LocaleData/cs/LC_MESSAGES/video.dvdrip.mo
%lang(de) %{perl_vendorlib}/LocaleData/de/LC_MESSAGES/video.dvdrip.mo
%lang(es) %{perl_vendorlib}/LocaleData/es/LC_MESSAGES/video.dvdrip.mo
%lang(fr) %{perl_vendorlib}/LocaleData/fr/LC_MESSAGES/video.dvdrip.mo
%lang(it) %{perl_vendorlib}/LocaleData/it/LC_MESSAGES/video.dvdrip.mo
%lang(sr) %{perl_vendorlib}/LocaleData/sr/LC_MESSAGES/video.dvdrip.mo
%{_bindir}/dr_exec
%{_bindir}/dr_progress
%{_bindir}/dr_splitpipe
%{_bindir}/dvdrip
%{_bindir}/dvdrip-master
%dir %{perl_vendorlib}/Video/
%{perl_vendorlib}/Video/DVDRip/
%{perl_vendorlib}/Video/DVDRip.pm
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-dvdrip.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/dvdrip.desktop}

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.52.6-2
- Cosmetic cleanup.

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

