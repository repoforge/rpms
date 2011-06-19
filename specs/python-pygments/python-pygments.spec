# $Id$
# Authority: dag

### EL6 ships with python-pygments-1.1.1-1.el6
%{?el6:# Tag: rfx}

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Pygments

Summary: Syntax highlighting engine written in Python
Name: python-pygments
Version: 1.4
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://pygments.org/

Source: http://cheeseshop.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
#BuildRequires: python-setuptools
#Requires: python-setuptools

%description
Pygments is a syntax highlighting engine written in Python. That means, it 
will take source code (or other markup) in a supported language and output 
a processed version (in different formats) containing syntax highlighting 
markup.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"

%{__install} -dp -m0755 %{buildroot}%{_mandir}/man1/
%{__mv} docs/pygmentize.1 %{buildroot}%{_mandir}/man1/pygmentize.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES LICENSE TODO docs/
%doc %{_mandir}/man1/pygmentize.1*
%{_bindir}/pygmentize
%{python_sitelib}/Pygments-%{version}-p*.egg-info/
%{python_sitelib}/pygments/

%changelog
* Thu May 26 2011 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Mon Jul 06 2009 Dag Wieers <dag@wieers.com> - 0.9-1
- Initial package. (using DAR)
