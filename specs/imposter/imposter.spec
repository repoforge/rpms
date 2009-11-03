# $Id$
# Authority: dag
# Upstream: <imposter-devel$lists,sourceforge,net>

%define desktop_vendor rpmforge

Summary: Standalone viewer for OpenOffice presentations
Name: imposter
Version: 0.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://imposter.sourceforge.net/

Source: http://dl.sf.net/sourceforge/imposter/imposter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
imposter is a standalone viewer for OpenOffice peresentations.

%prep
%setup

%{__cat} <<EOF >imposter.desktop
[Desktop Entry]
Name=Imposter Presentation Viewer
Comment=Display OpenOffice presentations
Exec=imposter
Icon=redhat-presentations.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Office;
MimeType=application/vnd.stardivision.impress;application/vnd.sun.xml.impress;
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 imposter.desktop %{buildroot}%{_datadir}/applications/imposter.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --delete-original             \
		--vendor %{desktop_vendor}                 \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		imposter.desktop
%endif

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/imposter
%{_datadir}/applications/%{desktop_vendor}-imposter.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
