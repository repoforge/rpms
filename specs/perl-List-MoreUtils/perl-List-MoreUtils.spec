# $Id$

# Authority: dries
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define real_name List-MoreUtils
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Additions to List::Util
Name: perl-List-MoreUtils
Version: 0.09
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-MoreUtils/

Source: http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/List-MoreUtils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provide the missing functionality from List::Util (see
"SUGGESTED ADDITIONS" in its manpage).

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
%{perl_vendorarch}/List/MoreUtils.pm
%{perl_vendorarch}/auto/List/MoreUtils
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
