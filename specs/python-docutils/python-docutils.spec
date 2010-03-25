# $Id$
# Authority: shuff
# Upstream: David Goodger <goodger$python,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name docutils

Summary: Python documentation processing utilities
Name: python-docutils
Version: 0.6
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://docutils.sourceforge.net/

Source: http://downloads.sourceforge.net/project/docutils/docutils/%{version}/docutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3, python-imaging
Requires: python >= 2.3, python-imaging

%description
The purpose of the Docutils project is to create a set of tools for processing
plaintext documentation into useful formats, such as HTML, XML, and LaTeX.
Support for the following sources has been implemented:

* Standalone files.
* PEPs (Python Enhancement Proposals).

Support for the following sources is planned:

* Inline documentation from Python modules and packages, extracted with
  namespace context.
* Email (RFC-822 headers, quoted excerpts, signatures, MIME parts).
* Wikis, with global reference lookups of "wiki links".
* Compound documents, such as multiple chapter files merged into a book.
* And others as discovered.


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
%doc BUGS.txt COPYING.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt
%doc THANKS.txt docs/ licenses/
%{python_sitelib}/*
%exclude %{python_sitelib}/*.pyo
%exclude %{python_sitelib}/*/*.pyo
%exclude %{python_sitelib}/*/*/*.pyo
%exclude %{python_sitelib}/*/*/*/*.pyo
%exclude %{python_sitelib}/*/*/*/*/*.pyo
%{_bindir}/*
%exclude %{_bindir}/*.pyo

%changelog
* Wed Mar 24 2010 Steve Huff <shuff@vecna.org> - 0.6-1
- Initial package.
