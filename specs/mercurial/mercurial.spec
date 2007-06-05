# $Id$
# Authority: dries
# Upstream: Matt Mackall <mpm$selenic,com>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')


Summary: Fast lightweight source control management system
Name: mercurial
Version: 0.9.3
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.selenic.com/mercurial/wiki/

Source: http://www.selenic.com/mercurial/release/mercurial-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python

%description
Mercurial is a fast, lightweight Source Control Management system designed 
for the efficient handling of very large distributed projects. 

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__make} install-doc PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}
# TODO: also install contrib, maybe in subpackage

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIBUTORS COPYING README 
%doc %{_mandir}/man1/hg*.1*
%doc %{_mandir}/man5/hg*.5*
%{_bindir}/hg
%{_bindir}/hgmerge
%{python_sitelib}/mercurial/
%{python_sitelib}/hgext/

%changelog
* Tue Jun 05 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Initial package.
