# $Id$
# Authority: dries
# Upstream: brouits$free,fr

Summary: Convert CSV files to LaTeX documents
Name: csv2latex
Version: 0.10
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://brouits.free.fr/csv2latex/

Source: http://brouits.free.fr/csv2latex/csv2latex_%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
csv2latex is a file format converter that converts a well formed CSV file
(like the ones exported from OpenOffice.org) to the LaTeX document format.

%prep
%setup

%build
gcc -Wall -o csv2latex csv2latex.c

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 csv2latex %{buildroot}%{_bindir}/csv2latex

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/csv2latex

%changelog
* Mon Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-2
- Source url fixed.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
