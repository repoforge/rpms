# Authority: freshrpms
# Dists: rh80 rh90

%define rname xmms
%define plugindir %(xmms-config --input-plugin-dir)

Summary: MP3 plugin for XMMS.
Name: xmms-mp3
Version: 1.2.7
Release: 0
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.xmms.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.xmms.org/files/1.2.x/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib-devel >= 1.2.2, gtk+-devel >= 1.2.2
BuildRequires: XFree86-devel, esound-devel, mikmod, arts-devel >= 1.0.1
Requires: %{rname} = %{epoch}:%{version}
Obsoletes: x11amp0.7-1-1 x11amp xmms-esd xmms-gl xmms-mikmod xmms-gnome

%description
This is the MP3 plugin for XMMS that was removed due the uncertain
patent/licensing issues.

%prep
%setup -n %{rname}-%{version}

%build
%configure --enable-kanji --enable-texthack --enable-arts-shared
%{__make} %{?_smp_mflags} -C Input/mpg123

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{plugindir}
%{__install} -m0755 Input/mpg123/.libs/libmpg123.{la,so} %{buildroot}%{plugindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Input/mpg123/README
%{plugindir}/*.so
%exclude %{plugindir}/*.la

%changelog
* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Initial package. (using DAR)
