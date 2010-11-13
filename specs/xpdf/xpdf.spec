# $Id$
# Authority: dag

### EL4 ships with xpdf-3.00-24.el4_8.1
%{?el4:# Tag: rfx}
### EL3 ships with xpdf-2.02-19.el3
%{?el3:# Tag: rfx}
### EL2 ships with xpdf-0.92-19.el2
%{?el2:# Tag: rfx}

%define desktop_vendor rpmforge

Summary: Portable Document Format (PDF) viewer
Name: xpdf
Epoch: 1
Version: 3.02
Release: 8%{?dist}
License: GPLv2
Group: Applications/Publishing
URL: http://www.foolabs.com/xpdf/

Source0: ftp://ftp.foolabs.com/pub/xpdf/xpdf-%{version}.tar.gz
Source3: ftp://ftp.foolabs.com/pub/xpdf/xpdf-chinese-simplified-2004-jul-27.tar.gz
Source4: ftp://ftp.foolabs.com/pub/xpdf/xpdf-chinese-traditional-2004-jul-27.tar.gz
Source5: ftp://ftp.foolabs.com/pub/xpdf/xpdf-japanese-2004-jul-27.tar.gz
Source6: ftp://ftp.foolabs.com/pub/xpdf/xpdf-korean-2005-jul-07.tar.gz
Source7: ftp://ftp.foolabs.com/pub/xpdf/xpdf-cyrillic-2003-jun-28.tar.gz
Source8: ftp://ftp.foolabs.com/pub/xpdf/xpdf-thai-2002-jan-16.tar.gz
Source11: xpdf.png
Source12: ftp://ftp.foolabs.com/pub/xpdf/xpdf-arabic-2003-feb-16.tar.gz
Source13: ftp://ftp.foolabs.com/pub/xpdf/xpdf-greek-2003-jun-28.tar.gz
Source14: ftp://ftp.foolabs.com/pub/xpdf/xpdf-hebrew-2003-feb-16.tar.gz
Source15: ftp://ftp.foolabs.com/pub/xpdf/xpdf-latin2-2002-oct-22.tar.gz
Source16: ftp://ftp.foolabs.com/pub/xpdf/xpdf-turkish-2002-apr-10.tar.gz
Patch0: xpdf-3.01-redhat-new.patch
Patch3: xpdf-2.02-ext.patch
Patch6: xpdf-3.00-core.patch
Patch7: xpdf-3.00-xfont.patch
Patch9: xpdf-3.00-papersize.patch
Patch10: xpdf-3.00-gcc4.patch
Patch11: xpdf-3.02-crash.patch
Patch12: xpdf-3.00-64bit.patch
Patch15: xpdf-3.01-nocmap.patch
Patch16: xpdf-3.02-fontlist.patch
Patch17: xpdf-3.02-x86_64-fix.patch
Patch18: xpdf-3.02-mousebuttons.patch
Patch19: xpdf-3.02-additionalzoom.patch
Patch20: xpdf-3.02-mousebuttons_view.patch
### Security patches
Patch100: ftp://ftp.foolabs.com/pub/xpdf/xpdf-%{version}pl1.patch
Patch101: ftp://ftp.foolabs.com/pub/xpdf/xpdf-%{version}pl2.patch
Patch102: ftp://ftp.foolabs.com/pub/xpdf/xpdf-%{version}pl3.patch
Patch103: ftp://ftp.foolabs.com/pub/xpdf/xpdf-%{version}pl4.patch
### Debian patches
Patch200: 02_permissions.dpatch
Patch201: 10_add_accelerators.dpatch
# Fix crash with ctrl-W in full screen mode
Patch202: fix-437725.dpatch
# Proper stream encoding on 64bit platforms
Patch203: fix-444648.dpatch
# Fix segfault in image handling
Patch204: fix-462544.dpatch
# Fix crash with "g" in full screen mode
Patch205: fix-479467.dpatch
### Remove password protection
Patch300: xpdf-3.02-ownerpw.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: xpdf-chinese-simplified = %{version}-%{release}
Obsoletes: xpdf-chinese-simplified
Provides: xpdf-chinese-traditional = %{version}-%{release}
Obsoletes: xpdf-chinese-traditional
Provides: xpdf-japanese = %{version}-%{release}
Obsoletes: xpdf-japanese
Provides: xpdf-korean = %{version}-%{release}
Obsoletes: xpdf-korean

BuildRequires: desktop-file-utils
BuildRequires: fileutils
BuildRequires: freetype-devel >= 2.1.7
BuildRequires: libpaper-devel
BuildRequires: libX11-devel
BuildRequires: openmotif-devel
BuildRequires: t1lib-devel
BuildRequires: wxGTK
Requires: poppler-utils
Requires: urw-fonts
Requires: xdg-utils
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi

%description
Xpdf is an open source viewer for Portable Document Format (PDF)
files.  (These are also sometimes also called 'Acrobat' files, from
the name of Adobe's PDF software.)  The Xpdf project also includes a
PDF text extractor, PDF-to-PostScript converter, and various other
utilities.

Xpdf runs under the X Window System on UNIX, VMS, and OS/2.  The non-X
components (pdftops, pdftotext, etc.) also run on Win32 systems and
should run on pretty much any system with a decent C++ compiler.

Xpdf is designed to be small and efficient.  It can use Type 1 or
TrueType fonts.

%prep
%setup -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 12 -a 13 -a 14 -a 15 -a 16
%patch0 -p1
%patch3 -p1 -b .ext
%patch6 -p1 -b .core
%patch7 -p1 -b .fonts
%patch9 -p1 -b .papersize
%patch10 -p1 -b .gcc4
%patch11 -p1 -b .crash
%patch12 -p1 -b .alloc
%patch15 -p1
%patch16 -p1 -b .fontlist
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

### security patches
%patch100 -p1 -b .security
%patch101 -p1 -b .security2
%patch102 -p1 -b .security3
%patch103 -p1 -b .security4

### debian patches
%patch200 -p1 -b .permissions
%patch201 -p1 -b .accelerators
%patch202 -p1 -b .fullscreen-crashfix
%patch203 -p1 -b .64bit-stream
%patch204 -p1 -b .segfaultfix
%patch205 -p1 -b .fullscreen-crashfix2

### Additional patches
%patch300 -p0 -b .owernpw

%{__cat} <<EOF >xpdf.desktop
[Desktop Entry]
Encoding=UTF-8
Categories=Application;Graphics;
Name=Xpdf PDF Viewer
Comment=View PDF files
Exec=xpdf
Terminal=0
Type=Application
Icon=xpdf.png
MimeType=application/pdf
EOF

%build
%configure \
    --enable-multithreaded \
    --enable-opi \
    --enable-wordlist \
    --with-appdef-dir="%{_datadir}/X11/app-defaults/" \
    --with-gzip \
    --with-freetype2-library="%{_libdir}" \
    --with-freetype2-includes="%{_includedir}/freetype2" \
    --with-t1-library \
    --with-x \
    --without-Xp-library
%{__make} %{?_smp_mflags}
%{__make} xpdf %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/arabic/
%{__cp} -av xpdf-arabic/* %{buildroot}%{_datadir}/xpdf/arabic/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/chinese-simplified/
%{__cp} -av xpdf-chinese-simplified/* %{buildroot}%{_datadir}/xpdf/chinese-simplified/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/chinese-traditional/
%{__cp} -av xpdf-chinese-traditional/* %{buildroot}%{_datadir}/xpdf/chinese-traditional/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/cyrillic/
%{__cp} -av xpdf-cyrillic/* %{buildroot}%{_datadir}/xpdf/cyrillic/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/greek/
%{__cp} -av xpdf-greek/* %{buildroot}%{_datadir}/xpdf/greek/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/hebrew/
%{__cp} -av xpdf-hebrew/* %{buildroot}%{_datadir}/xpdf/hebrew/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/japanese/
%{__cp} -av xpdf-japanese/* %{buildroot}%{_datadir}/xpdf/japanese/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/korean/
%{__cp} -av xpdf-korean/* %{buildroot}%{_datadir}/xpdf/korean/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/latin2/
%{__cp} -av xpdf-latin2/* %{buildroot}%{_datadir}/xpdf/latin2/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/thai/
%{__cp} -av xpdf-thai/* %{buildroot}%{_datadir}/xpdf/thai/

%{__install} -d -m0755 %{buildroot}%{_datadir}/xpdf/turkish/
%{__cp} -av xpdf-turkish/* %{buildroot}%{_datadir}/xpdf/turkish/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/xpdf/
for lang in arabic chinese-simplified chinese-traditional cyrillic greek hebrew japanese korean latin2 thai turkish; do
     %{__mv} -v %{buildroot}%{_datadir}/xpdf/$lang/README README.$lang
     %{__mv} -v %{buildroot}%{_datadir}/xpdf/$lang/add-to-xpdfrc %{buildroot}%{_sysconfdir}/xpdf/add-to-xpdfrc.$lang
done

### xpdfrc cleanup
%{__perl} -pi -e 's|/usr/local/share/|%{_datadir}/|g' %{buildroot}%{_sysconfdir}/{xpdfrc,xpdf/*}

### CJK are already in the file
for lang in arabic cyrillic greek hebrew latin2 thai turkish; do
    echo -e "# $lang\ninclude %{_sysconfdir}/xpdf/add-to-xpdfrc.$lang" >>%{buildroot}%{_sysconfdir}/xpdfrc
done

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}       \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    xpdf.desktop
%{__install} -Dp -m0644 %{SOURCE11} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/xpdf.png

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &>/dev/null ||:

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &>/dev/null ||:

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE CHANGES COPYING INSTALL README*
%doc %{_mandir}/man1/pdftoppm.1*
%doc %{_mandir}/man1/xpdf.1*
%doc %{_mandir}/man5/xpdfrc.5*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdfrc
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/
%{_bindir}/pdftoppm
%{_bindir}/xpdf
%{_datadir}/applications/%{desktop_vendor}-xpdf.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpdf.png
%{_datadir}/xpdf/
### These files are provided by poppler
%exclude %{_bindir}/pdffonts
%exclude %{_bindir}/pdfimages
%exclude %{_bindir}/pdfinfo
#exclude %{_bindir}/pdftoppm
%exclude %{_bindir}/pdftops
%exclude %{_bindir}/pdftotext
%exclude %{_mandir}/man1/pdffonts.1*
%exclude %{_mandir}/man1/pdfimages.1*
%exclude %{_mandir}/man1/pdfinfo.1*
#exclude %{_mandir}/man1/pdftoppm.1*
%exclude %{_mandir}/man1/pdftops.1*
%exclude %{_mandir}/man1/pdftotext.1*

%changelog
* Thu Aug 05 2010 Dag Wieers <dag@wieers.com> - 1:3.02-8
- Fix /usr/local/share/xpdf references in /etc/xpdf/

* Wed Aug 04 2010 Dag Wieers <dag@wieers.com> - 1:3.02-7
- Added epoch for compatibility with RHEL5's poppler-utils.

* Tue Aug 03 2010 Dag Wieers <dag@wieers.com> - 3.02-6
- Imported package and added patches from fedora.

* Thu Nov 20 2008 Geerd-Dietger Hoffmann <ribalba@gmail.com> - 3.02-5
- Added 3.02pl2.patch.

* Fri Aug 24 2007 Martin Brisby <rpms@mbrisby.org>
- Added 3.02pl1 patch.

* Sat Jun 16 2007 Martin Brisby <rpms@mbrisby.org>
- Initial specfile.
