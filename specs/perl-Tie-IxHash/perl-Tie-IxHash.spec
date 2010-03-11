# $Id$
# Authority: dries
# Upstream: Alexandr Ciornii <alexchorny@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-IxHash

Summary: Ordered associative arrays for Perl
Name: perl-Tie-IxHash
Version: 1.22
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-IxHash/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
If you have been led to believe that associative arrays in perl
don't preserve order, and if you have ever craved for that feature,
this module is for you.  Simply declare a "tie" for the hash variable
that you want to be order-preserving, and forget that limitation
ever existed.  You can do other nifty things with the tied hash object
that you may be used to doing with arrays, like Push(), Pop() and
Splice().

If you don't know what "tie" means, you should look at the
perltie(1) manpage in a recent perl distribution, or in the
index of one of the numerous books on perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/IxHash.pm

%changelog
* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
