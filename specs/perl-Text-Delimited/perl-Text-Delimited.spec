# $Id$

# Authority: dries
# Upstream: Phillip Pollard <bennie$cpan,org>

%define real_name Text-Delimited
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module for parsing delimited text files
Name: perl-Text-Delimited
Version: 1.93
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Delimited/

Source: http://search.cpan.org/CPAN/authors/id/B/BE/BENNIE/Text-Delimited-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Delimited.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.93-1
- Initial package.
