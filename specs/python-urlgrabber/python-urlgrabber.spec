# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name urlgrabber

Summary: High-level cross-protocol url-grabber
Name: python-urlgrabber
Version: 2.9.7
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://linux.duke.edu/projects/urlgrabber/

Source: http://linux.duke.edu/projects/urlgrabber/download/urlgrabber-%{version}.tar.gz
Patch: python-urlgrabber-2.9.6-reget.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Provides: urlgrabber
BuildRequires: python

%description
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .reget

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README TODO
%{_bindir}/urlgrabber
%{python_sitelib}/urlgrabber/
%ghost %{python_sitelib}/urlgrabber/*.pyo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.9.7-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 2.9.7-1
- Initial package. (using DAR)

