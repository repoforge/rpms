# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Simple graphical text editor
Name: leafpad
Version: 0.8.9
Release: 2
License: GPL
Group: Applications/Editors
URL: http://tarot.freeshell.org/leafpad/

Source: http://savannah.nongnu.org/download/leafpad/leafpad-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_freedesktop:Requires: desktop-file-utils}

%description
Leafpad is a GTK+ based simple text editor. The user interface is similar to
Notepad. It aims to be lighter than GEdit and KWrite, and to be as useful as
them.

%prep
%setup
%{__cat} <<EOF >>leafpad.desktop
StartupNotify=true
GenericName=Text Editor
EOF

%build
%configure --enable-chooser
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
	desktop-file-install --delete-original             \
		--vendor=%{desktop_vendor}                 \
		--add-category GTK                         \
		--dir %{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/leafpad.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database || :

%postun
update-desktop-database || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_bindir}/leafpad
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-leafpad.desktop}
%{?_without_freedesktop:%{_datadir}/applications/leafpad.desktop}
%{_datadir}/pixmaps/leafpad.png
%{_datadir}/pixmaps/leafpad.xpm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.8.9-2
- Define %%{desktop_vendor}.

* Wed Feb 21 2007 Dag Wieers <dag@wieers.com> - 0.8.9-1
- Initial package. (using DAR)
