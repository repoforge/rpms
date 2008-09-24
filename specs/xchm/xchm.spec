# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: GUI front-end to chmlib
Name: xchm
Version: 1.14
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://xchm.sourceforge.net/

Source: http://dl.sf.net/xchm/xchm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%{_arch}-root

BuildRequires: chmlib-devel
BuildRequires: desktop-file-utils
BuildRequires: wxGTK-devel

%description
xCHM is a wxWidgets-based .chm viewer. xCHM can show the contents tree if
one is available, print the displayed page, change fonts faces and size,
work with bookmarks, do the usual history stunts (forward, back, home),
provide a searchable index and seach for text in the whole book. The
search is a fast B-tree search, based on the internal $FIftiMain file
found inside indexed .chm archives, and it can be customized to search in
content or just the topics' titles.

%prep
%setup

%{__cat} <<EOF >xchm.desktop
[Desktop Entry]
Encoding=UTF-8
Name=xCHM
GenericName=chm file viewer
Comment=GUI front-end to chmlib
Exec=xchm
Icon=xchm
Terminal=false
Type=Application
MimeType=application/x-chm;
Categories=Utility;
EOF

%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

for res in 16 32 48 128; do
    %{__install} -Dp -m0644 art/xchm-$res.xpm %{buildroot}%{_datadir}/icons/hicolor/${res}x$res/apps/xchm.xpm
    %{__install} -Dp -m0644 art/xchmdoc-$res.xpm %{buildroot}%{_datadir}/icons/hicolor/${res}x$res/mimetypes/application-x-chm.xpm
    %{__ln_s} -f application-x-chm.xpm %{buildroot}%{_datadir}/icons/hicolor/${res}x$res//mimetypes/gnome-mime-application-x-chm.xpm
done

%{__install} -dp -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    xchm.desktop

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null ||:

%files -f %{name}.lang
%defattr(-, root, root,0755)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/xchm
%{_datadir}/applications/%{desktop_vendor}-xchm.desktop
%{_datadir}/icons/hicolor/

%changelog
* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 1.14-1
- Initial package. (using DAR)
