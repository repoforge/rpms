# $Id$
# Authority: dag

%define xmms_visualdir %(xmms-config --visualization-plugin-dir)
%define real_name goom

Summary: Neat visual plugin for XMMS
Name: xmms-goom
Version: 1.99.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://goom.sourceforge.net/

Source: http://ios.free.fr/goom/devel/goom-%{version}-src.tgz
Patch: goom-1.99.4-gcc3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel, SDL-devel, gtk+-devel


%description
A great visual plugins for XMMS.


%prep
%setup -n %{real_name}-%{version}
%patch0


%build
./configure \
	--enable-shared \
	--libdir="%{xmms_visualdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_visualdir}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING KNOWNBUGS NEWS README
%{xmms_visualdir}/*.so
%exclude %{xmms_visualdir}/*.la


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.99.4-0.2
- Rebuild for Fedora Core 5.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.99.4-0
- Initial package. (using DAR)
