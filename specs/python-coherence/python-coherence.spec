# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Coherence

Summary: Python framework to participate in digital living networks
Name: python-coherence
Version: 0.5.8
Release: 1%{?dist}
License: MIT
Group: Development/Languages
URL: https://coherence.beebits.net/

Source: http://coherence.beebits.net/download/Coherence-0.5.8.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-configobj
Requires: python-setuptools

Obsoletes: coherence < 0.2.1-2
Obsoletes: Coherence < 0.2.1-3
Obsoletes: python-Coherence <= %{version}-%{release}
Provides: python-Coherence = %{version}-%{release}

%description
Coherence is a framework written in Python enabling applications to participate
in digital living networks, such as the UPnP universe.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENCE README docs/*
%{_bindir}/coherence
%{python_sitelib}/Coherence-*.egg-info/
%{python_sitelib}/coherence/
%exclude %{_bindir}/applet-coherence
%exclude %{python_sitelib}/misc/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.5.8-1
- Initial package. (based on fedora)
