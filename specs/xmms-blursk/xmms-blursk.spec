# $Id$
# Authority: dag

%define real_name Blursk
%define xmms_visualdir %(xmms-config --visualization-plugin-dir)

Summary: Visualization plugin for the Linux XMMS music player
Name: xmms-blursk
Version: 1.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.cs.pdx.edu/~kirkenda/blursk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cs.pdx.edu/~kirkenda/blursk/Blursk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2.0, gtk+-devel >= 1.2.0


%description
Blursk is a visualization plugin for the Linux XMMS music player. It was
inspired by the "Blur Scope" plugin, but Blursk goes far beyond that.

It supports a wide variety of colormaps, blur patterns, plotting styles,
and other options. The only things that haven't changed are portions of
the XMMS interface and configuration code.


%prep
%setup -n %{real_name}-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 .libs/libblursk.so %{buildroot}%{xmms_visualdir}/libblursk.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{xmms_visualdir}/*.so


%changelog
* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Initial package. (using DAR)
