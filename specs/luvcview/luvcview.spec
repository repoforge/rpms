# $Id$
# Authority: dag

%define real_name luvcview

Summary: Tool to test uvcview devices
Name: luvcview
%define real_version 20070512
Version: 0.0.20070512
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://openfacts.berlios.de/index-en.phtml?title=Linux+UVC

Source: http://mxhaard.free.fr/spca50x/Investigation/uvc/luvcview-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel

%description
luvcview is a tool to test uvcview devices.

%prep
%setup -n %{name}-%{real_version}

%build
export CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 luvcview %{buildroot}%{_bindir}/luvcview

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README ToDo
%{_bindir}/luvcview

%changelog
* Fri Dec 19 2008 Dag Wieers <dag@wieers.com> - 0.0.20070512-1
- Initial package. (using DAR)
