# $Id$

# Authority: dries
# Upstream: Tye McQueen <tyemq$cpan,org>

%define real_name Algorithm-Diff
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Compute intelligent differences between two files or lists
Name: perl-Algorithm-Diff
Version: 1.1901
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Diff/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TY/TYEMQ/Algorithm-Diff-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a module for computing the difference between two files, two
strings, or any other two lists of things.  It uses an intelligent
algorithm similar to (or identical to) the one used by the Unix "diff"
program.  It is guaranteed to find the *smallest possible* set of
differences.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Algorithm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.1901-1
- Initial package.

