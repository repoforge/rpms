# $Id$
# Authority: shuff
# Upstream: Mitch Garnaat <mitch$garnaat,org>

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name boto

Summary: Python interface to Amazon Web Services
Name: python-boto
Version: 1.9b
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://code.google.com/p/boto/

Source: http://boto.googlecode.com/files/boto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4

Provides: boto
Obsoletes: boto <= %{version}-%{release}

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
At the moment, boto supports:

* S3 (Simple Storage Service) via the REST API
* SQS (SimpleQueue Service) via the Query API
* EC2 (Elastic Compute Cloud) via the Query API
* Mechanical Turk via the Query API
* SimpleDB via the Query API.
* CloudFront via the REST API
* CloudWatch via the Query API
* AutoScale via the Query API
* Elastic Load Balancer via the Query API

The intent is to support additional services in the future.


%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README docs/
%{_bindir}/*
%dir %{python_sitelib}/boto/
%{python_sitelib}/boto/*.py
%{python_sitelib}/boto/*.pyc
%{python_sitelib}/boto/*/*.py
%{python_sitelib}/boto/*/*.pyc
%{python_sitelib}/boto/*/*/*.py
%{python_sitelib}/boto/*/*/*.pyc
%{python_sitelib}/boto/*/*/*/*.py
%{python_sitelib}/boto/*/*/*/*.pyc
%ghost %{python_sitelib}/boto/*.pyo
%ghost %{python_sitelib}/boto/*/*.pyo
%ghost %{python_sitelib}/boto/*/*/*.pyo
%ghost %{python_sitelib}/boto/*/*/*/*.pyo
%exclude %{python_sitelib}/boto-%{version}-py*.egg-info/

%changelog
* Tue Aug 10 2010 Steve Huff <shuff@vecna.org> - 1.9b-1
- Initial package.
