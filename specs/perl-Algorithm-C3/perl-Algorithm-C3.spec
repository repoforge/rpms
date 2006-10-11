# $Id$
# Authority: dries
# Upstream: Brandon L Black <blblack$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-C3

Summary: Module for merging hierarchies using the C3 algorithm
Name: perl-Algorithm-C3
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-C3/

Source: http://search.cpan.org/CPAN/authors/id/B/BL/BLBLACK/Algorithm-C3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Test::More)

%description
C3 is the name of an algorithm which aims to provide a sane method
resolution order under multiple inheritence. It was first introduced
in the langauge Dylan (see links in the L<SEE ALSO> section), and
then later adopted as the preferred MRO (Method Resolution Order)
for the new-style classes in Python 2.3. Most recently it has been
adopted as the 'canonical' MRO for Perl 6 classes, and the default
MRO for Parrot objects as well.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Algorithm::C3*
%dir %{perl_vendorlib}/Algorithm
%{perl_vendorlib}/Algorithm/C3.pm

%changelog
* Sat Jul 15 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.05-1
- Initial packaging
