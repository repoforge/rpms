# $Id$

# Authority: dag

# Upstream: Roman Hochleitner <roman@mars.tuwien.ac.at>

%define rname NuppelVideo
%define rversion 0.52a

Summary: NuppelVideo recording tool.
Name: nuppelvideo
Version: 0.51.81
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://frost.htu.tuwien.ac.at/~roman/nuppelvideo/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://frost.htu.tuwien.ac.at/~roman/%{name}/%{rname}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
NuppelVideo recording tool.

%prep
%setup -n %{rname}-%{rversion}

%build
%{__perl} -pi -e 's|/usr/local/bin|%{buildroot}%{_bindir}|' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* README*
%{_bindir}/*

%changelog
* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 0.51.81
- Initial package. (using DAR)
