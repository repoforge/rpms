# $Id$
# Authority: matthias
# Upstream: Peter Eisenlohr <peter$eisenlohr,org>

%define output_plugin_dir %(pkg-config --variable=output_plugin_dir audacious 2>/dev/null || echo %{_libdir}/audacious/Output)

Summary: Crossfade output plugin for Audacious
Name: audacious-crossfade
Version: 0.3.11
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.eisenlohr.org/xmms-crossfade/
Source: http://www.eisenlohr.org/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious
BuildRequires: audacious-devel, libsamplerate-devel

%description
A neat crossfade plugin for Audacious featuring crossfading and continuous
output between songs and a gap-killer.


%prep
%setup -n xmms-crossfade-%{version}


%build
%configure \
    --enable-player=audacious \
    --disable-oss \
    --libdir=%{output_plugin_dir}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall libdir=%{buildroot}%{output_plugin_dir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{output_plugin_dir}/libcrossfade.so
%exclude %{output_plugin_dir}/libcrossfade.la


%changelog
* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 0.3.11-1
- Initial RPM release based on the xmms-crossfade spec (same source).
- Disable internal OSS output since we want to use Alsa by default.

