# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define rversion 508

Summary: Adobe Reader for viewing PDF files.
Name: acroread
Version: 5.0.8
Release: 1
License: Commercial, Freely Distributable
Group: Applications/Publishing
URL: http://www.adobe.com/products/acrobat/readermain.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.adobe.com/pub/adobe/acrobatreader/unix/5.x/linux-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

ExclusiveArch: i386
BuildRequires: perl
Obsoletes: acrobat

%description
Adobe Reader is part of the Adobe Acrobat family of software,
which lets you view, distribute, and print documents in Portable
Document Format (PDF)--regardless of the computer, operating system,
fonts, or application used to create the original file.

PDF files retain all the formatting, fonts, and graphics of the
original document, and virtually any PostScript(TM) document can
be converted into a PDF file. Adobe Acrobat Reader have a plug-in
for Netscape Navigator to to view PDF files inline

%package -n mozilla-acroread
Summary: Adobe Reader plug-in for viewing PDF files with the mozilla browser.
Group: Applications/Internet
Requires: %{name} = %{version}, mozilla
Provides: %{name}-plugin = %{version}-%{release}
Obsoletes: %{name}-plugin < %{version}

%description -n mozilla-acroread
This package provides the Adobe Reader plugin for mozilla.

%prep
%setup -c

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Adobe Reader
Comment=View and print PDF files
Exec=acroread
Terminal=false
Type=Application
Icon=acroread.png
MimeType=application/pdf
Categories=Application;Graphics;
EOF

%{__cat} <<EOF >WebLink
*LinkDisplay:	CTRL
*OpenURL:	NO
*IsMapped:	NO
*Progress:	NO
*Toolbar:	YES
*SelectedBrowser:	/usr/bin/htmlview	
*SelectedDriver:	Netscape
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/acroread/ \
			%{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/ \
			%{buildroot}%{_libdir}/mozilla/plugins/ \
			%{buildroot}%{_libdir}/netscape/plugins/
%{__tar} -xvf COMMON.TAR -C %{buildroot}%{_libdir}/acroread/
%{__tar} -xvf LINUXRDR.TAR -C %{buildroot}%{_libdir}/acroread/

%{__mv} -f %{buildroot}%{_libdir}/acroread/bin/acroread.sh %{buildroot}%{_libdir}/acroread/bin/acroread

### Fixup path and fixed LANG/LC_ALL settings until Adobe adds Unicode locale support
%{__perl} -pi -e 's|^install_dir=.*$|install_dir=%{_libdir}/acroread/Reader\n
NLANG="\${LANG//.UTF-8/.ISO8859-1}"
export LANG="\${NLANG:-C}"
NLC_ALL="\${LC_ALL//.UTF-8/.ISO8859-1}"
export LC_ALL="\${NLC_ALL:-C}"|' \
	%{buildroot}%{_libdir}/acroread/bin/acroread

### Shutup some rpm permission warnings
%{__chmod} +x %{buildroot}%{_libdir}/acroread/Reader/*/lib/lib*.so* %{buildroot}%{_libdir}/acroread/Browsers/*/*.so

%{__install} -m0644 WebLink %{buildroot}%{_libdir}/acroread/Reader/intellinux/app-defaults/

### Make links
%{__ln_s} -f %{_libdir}/acroread/bin/acroread %{buildroot}%{_bindir}/
%{__ln_s} -f %{_libdir}/acroread/Reader/intellinux/app-defaults/AcroRead %{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/
%{__ln_s} -f %{_libdir}/acroread/Reader/intellinux/app-defaults/WebLink %{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/
%{__ln_s} -f %{_libdir}/acroread/Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/netscape/plugins/
%{__ln_s} -f %{_libdir}/acroread/Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/mozilla/plugins/

### Strip binaries and libraries
#%{__strip} %{buildroot}%{_libdir}/acroread/Reader/intellinux/bin/acroread %{buildroot}%{_libdir}/acroread/Reader/intellinux/lib/*.so.*

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Graphics/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Graphics/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor net                  \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README *.TXT 
%{_bindir}/*
%{_libdir}/acroread/
%{_prefix}/X11R6/lib/X11/app-defaults/*
%if %{dfi}
        %{_datadir}/gnome/apps/Graphics/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files -n mozilla-acroread
%{_libdir}/mozilla/plugins/*
%{_libdir}/netscape/plugins/*

%changelog
* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 5.0.8-1
- Added fix to make locale settings still work. (Fernando Lozano)

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 5.0.8-0
- Added exports for LANG and LC_ALL, just in case. (Axel Thimm)
- Updated to release 5.0.8.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 5.0.7-2
- Fixed Unicode locale support, again. (Matthew Mastracci)

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 5.0.7-1
- Put mozilla plugins into a seperate package.
- Improved the desktop file.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 5.0.7-0
- Initial package. (using DAR)
