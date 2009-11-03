# $Id$
# Authority: matthias

%define aud_general %(pkg-config --variable=general_plugin_dir audacious)

Summary: iTouch keyboard control plugin for the Audacious media player
Name: audacious-itouch
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/itouch-control
Source: http://dl.sf.net/itouch-control/itouch-control-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious
BuildRequires: audacious-devel

%description
With this Audacious plugin you can take advantage of the multimedia (playback
and volume control) keys on your Logitech iTouch or compatible keyboard. When
the plugin is used you can use the keys regardless of the current input focus.
The plugin won't work if some other application (eg. xscreensaver) has grabbed
the keyboard.


%prep
%setup -n itouch-control-%{version}


%build
%configure \
    --libdir=%{aud_general}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    libdir=%{buildroot}%{aud_general}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{aud_general}/libitouchctrl.so
%exclude %{aud_general}/libitouchctrl.a
%exclude %{aud_general}/libitouchctrl.la


%changelog
* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 0.1.0-1
- Switch from the obsolete plugin to a current itouch-control version.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.1-5
- Add configdb patch to make it build with the latest audacious.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.1-4
- Release bump to drop the disttag number in FC5 build.

* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 0.1-3
- Rebuild against audacious 0.2.2 since the main .so lib isn't versionned
  anymore (thus the requirement here has broke).

* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 0.1-2
- Rebuild against proper FC4 gtk2 to fix unexisting dependencies.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.1-1
- Initial RPM release based on bmp-itouch.
- Something is weird, as the build can sometimes fail ("@CATALOGS@")...

