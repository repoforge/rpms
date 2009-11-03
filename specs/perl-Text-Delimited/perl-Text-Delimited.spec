# $Id$
# Authority: dries
# Upstream: Phillip Pollard <bennie$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Delimited

Summary: Module for parsing delimited text files
Name: perl-Text-Delimited
Version: 2.00
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Delimited/

Source: http://www.cpan.org/modules/by-module/Text/Text-Delimited-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::Delimited provides a programattical interface to data stored in
delimited text files. It is dependant upon the first row of the text
file containing header information for each corresponding "column" in
the remainder of the file.

After instancing, for each call to Read the next row's data is returned
as a hash reference. The individual elements are keyed by their
corresonding column headings.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Delimited.pm

%changelog
* Fri Sep 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Updated to release 2.00.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.93-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.93-1
- Initial package.
