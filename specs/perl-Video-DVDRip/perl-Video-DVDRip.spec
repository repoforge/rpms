# $Id$
# Authority: matthias

%define desktop_vendor  freshrpms

%define perl_sitelib    %(eval "`perl -V:installsitelib`"; echo $installsitelib)
%define __find_provides /usr/lib/rpm/find-provides.perl

Summary: DVD ripping graphical tool using transcode
Name: perl-Video-DVDRip
Version: 0.50.18
Release: 1
License: Artistic
Group: Applications/Multimedia
Source: http://www.exit1.org/dvdrip/dist/Video-DVDRip-%{version}.tar.gz
URL: http://www.exit1.org/dvdrip/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
AutoReq: no
Requires: transcode >= 0.6.3
Requires: Gtk-Perl, ImageMagick, ogmtools, subtitleripper, vcdimager, xvidcore
BuildRequires: Gtk-Perl, desktop-file-utils

%description
dvd::rip is a Perl Gtk+ based DVD copy program built on top of a low level
DVD Ripping API, which uses the Linux Video Stream Processing Tool transcode.


%prep
%setup -n Video-DVDRip-%{version}


%build
perl Makefile.PL
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    INSTALLSCRIPT=%{buildroot}%{_bindir} \
    INSTALLSITELIB=%{buildroot}%{perl_sitelib} \
    INSTALLSITEARCH=%{buildroot}%{perl_sitearch} \
    INSTALLMAN1DIR=%{buildroot}%{_mandir}/man1 \
    INSTALLSITEMAN1DIR=%{buildroot}%{_mandir}/man1 \
    INST_MAN1DIR=%{buildroot}%{_mandir}/man1 \
    INSTALLMAN3DIR=%{buildroot}%{_mandir}/man3 \
    INSTALLSITEMAN3DIR=%{buildroot}%{_mandir}/man3 \
    INST_MAN3DIR=%{buildroot}%{_mandir}/man3

# Unpackaged strange files!
%{__rm} -f %{buildroot}%{_mandir}/man?/.exists* || :

# Unneeded, all is in sitelib
%{__rm} -rf %{buildroot}%{perl_sitearch}

# Desktop entry
cat > dvdrip.desktop << EOF
[Desktop Entry]
Name=DVD Ripper and Encoder
Comment=Backup and compression utility for DVDs
Exec=dvdrip
Icon=%{perl_sitelib}/Video/DVDRip/icon.xpm
Terminal=0
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category AudioVideo                                       \
  dvdrip.desktop

# Add Red Hat NPTL workaround
perl -pi -e 's/BEGIN {\n/BEGIN {\n\t# Workaround for RH9 NPTL bug\n\t\$ENV{LD_ASSUME_KERNEL} = "2.2.5";\n/g' %{buildroot}%{_bindir}/dvdrip


%clean 
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{perl_sitelib}/Video/*
%{_datadir}/applications/*dvdrip.desktop
%{_mandir}/man*/*


%changelog
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

