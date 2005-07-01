# $Id$
# Authority: dries
# Upstream: brouits$free,fr

Summary: Convert CSV files to LaTeX documents
Name: csv2latex
Version: 0.7
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://brouits.free.fr/csv2latex/

Source: csv2latex-0.7.tar.gz
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
* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
