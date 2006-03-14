# $Id$
# Authority: matthias

%define aud_general %(pkg-config --variable=general_plugin_dir audacious)
%define aud_datadir %(pkg-config --variable=data_dir audacious)

Summary: iTouch keyboard control plugin for the Audacious media player
Name: audacious-itouch
Version: 0.1
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://nedudu.hu/?page_id=11
Source: http://nedudu.hu/downloads/audacious-itouch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious
BuildRequires: audacious-devel, gettext-devel, bison

%description
With this Audacious plugin you can take advantage of the multimedia (playback
and volume control) keys on your Logitech iTouch or compatible keyboard. When
the plugin is used you can use the keys regardless of the current input focus.
The plugin won't work if some other application (eg. xscreensaver) has grabbed
the keyboard.


%prep
%setup
# Workaround... but is this even correct?
%{__cp} -a po/Makefile.in.in po/Makefile.in


%build
%configure \
    --libdir=%{aud_general} \
    --datadir=%{aud_datadir}
# Build "sometimes" fails, so remove %{?_smp_mflags}, although it seems like
# that's not it.
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    libdir=%{buildroot}%{aud_general} \
    datadir=%{buildroot}%{aud_datadir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{aud_general}/libitouch.so
%exclude %{aud_general}/libitouch.la
%config %{aud_datadir}/audacious-itouch.config


%changelog
* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 0.2-3
- Rebuild against audacious 0.2.2 since the main .so lib isn't versionned
  anymore (thus the requirement here has broke).

* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 0.2-2
- Rebuild against proper FC4 gtk2 to fix unexisting dependencies.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.1-1
- Initial RPM release based on bmp-itouch.
- Something is weird, as the build can sometimes fail ("@CATALOGS@")...

