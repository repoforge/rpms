# $Id$
# Authority: matthias

Summary: Edward Loper's Python API documentation generation tool
Name: epydoc
Version: 2.1
Release: 3
Group: Development/Tools
License: MIT
URL: http://epydoc.sourceforge.net/
Source: http://dl.sf.net/epydoc/epydoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python, python-devel
BuildArch: noarch

%description
Epydoc  is a tool for generating API documentation for Python modules,
based  on their docstrings. For an example of epydoc's output, see the
API  documentation for epydoc itself (html, pdf). A lightweight markup
language  called  epytext can be used to format docstrings, and to add
information  about  specific  fields,  such as parameters and instance
variables.    Epydoc    also   understands   docstrings   written   in
ReStructuredText, Javadoc, and plaintext.


%prep
%setup -q


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
# Also install the man pages
%{__install} -Dp man/epydoc.1    %{buildroot}%{_mandir}/man1/epydoc.1
%{__install} -Dp man/epydocgui.1 %{buildroot}%{_mandir}/man1/epydocgui.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE.TXT README.TXT doc/
%{_bindir}/epydoc
%{_bindir}/epydocgui
%{_prefix}/lib/python?.?/site-packages/epydoc/
%{_mandir}/man1/epydoc.1*
%{_mandir}/man1/epydocgui.1*


%changelog
* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.1-3
- Fix for building on 64bit hosts (lib64 vs. lib).

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 2.1-2
- Make the package noarch as it contains no binaries.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 2.1-1
- Picked up and rebuilt.
- Added doc and man pages.

* Fri May 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.1-0.fdr.1: Initial package

