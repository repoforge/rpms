Name:		xournal
Version:	0.4.2.1
Release:	1%{?dist}
Summary:	Xournal notetaking, sketching and PDF annotation

Group:		Applications/Editors
License:	GPLv2
URL:		http://xournal.sourceforge.net/
Source0:	http://downloads.sourceforge.net/xournal/%{name}-%{version}.tar.gz
Source1:	xournal.desktop
Source2:	xournal.xml
Source3:	x-xoj.desktop
Patch0:		xournal-configure.in-freetype.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gtk2-devel >= 2.4.0 
BuildRequires:	libgnomecanvas-devel >= 2.4.0 
BuildRequires:	libgnomeprintui22-devel >= 2.0.0 
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick

Requires:	poppler-utils
Requires:	ghostscript

%description
Xournal is an application for notetaking, sketching, keeping a journal and 
annotating PDFs. Xournal aims to provide superior graphical quality (subpixel 
resolution) and overall functionality.

%prep
%setup -q
%patch

%build
NOCONFIGURE=1 ./autogen.sh
CFLAGS="%optflags -DPACKAGE_LOCALE_DIR=\\\"\"%{_datadir}/locale\"\\\" -DPACKAGE_DATA_DIR=\\\"\"%{_datadir}\"\\\"" %configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

# xournal icons and mime icons
# create 16x16, 32x32, 64x64, 128x128 icons and copy the 48x48 icon
for s in 16 32 48 64 128 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	convert -scale ${s}x${s} \
		pixmaps/%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
	%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	pushd ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	%{__ln_s} ../apps/xournal.png application-x-xoj.png
	%{__ln_s} application-x-xoj.png gnome-mime-application-x-xoj.png
	popd
done

# Desktop entry
%{__install} -p -m 0644 -D pixmaps/xournal.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/xournal.png
desktop-file-install --vendor fedora \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
	%{SOURCE1}

# GNOME (shared-mime-info) MIME type registration
%{__install} -p -m 0644 -D %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/mime/packages/xournal.xml

# KDE (legacy) MIME type registration
%{__install} -p -m 0644 -D %{SOURCE3} ${RPM_BUILD_ROOT}%{_datadir}/mimelnk/application/x-xoj.desktop


%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/xournal
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/*x*/mimetypes/application-x-xoj.png
%{_datadir}/icons/hicolor/*x*/mimetypes/gnome-mime-application-x-xoj.png
%{_datadir}/pixmaps/xournal.png
%{_datadir}/applications/fedora-xournal.desktop
%{_datadir}/mime/packages/xournal.xml
%{_datadir}/mimelnk/application/x-xoj.desktop
%{_datadir}/xournal/
%doc AUTHORS ChangeLog COPYING



%changelog
* Mon Apr  7 2008 Jeremy Katz <katzj@redhat.com> - 0.4.2.1-1
- Update to 0.4.2.1 to fix problems with newer xorg

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-4
- Autorebuild for GCC 4.3

* Wed Oct 10 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-3
- Changed permission on xournal.png from 0755 to 0644

* Fri Sep 21 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-2
- Added freetype to build requires
- Created patch to add freetype to configure.in pkgconfig

* Thu Sep 20 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-1
- New upstream release
- Changed source to use name and version variables
- Updated xournal.desktop to reflect upstream changes
- Updated x-xoj.desktop to reflect upstream changes
- Updated license to reflect specific GPL version

* Mon Jun 11 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-5
- Added Requires for poppler-utils (#243750)
- Added Requires for ghostscript

* Wed May 30 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-4
- Added optflags and PACKAGE_DATA_DIR to CFLAGS

* Tue May 29 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-3
- Changed all commands to macros
- Removed icon sources and create icons in spec from xournal icon
- Added 64x64 and 128x128 icons
- Consolidated icon directories with wildcards
- Added timestamp preservation to install
- Removed desktop categories Application and X-Fedora
- Added NOCONFIGURE to autogen.sh to stop auto-conf from running twice
- Removed desktop-file-utils post and postun requires
- Removed manual from doc section; it is already installed by the package
- Changed xournal.desktop, xournal.xml and x-xoj.desktop from here documents to files
- Add ImageMagick buildrequires for convert command
- Separated BuildRequires into one per line for easier reading
- Added PACKAGE_LOCALE_DIR CFLAG to configure

* Fri May 18 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-2
- Added mimetype support for gnome and kde
- Made xournal.desktop a here document

* Sat May 12 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-1
- Initial version

