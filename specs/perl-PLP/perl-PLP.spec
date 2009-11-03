# $Id$
# Authority: dries
# Upstream: Juerd Waalboer <spamcollector_cpan$juerd,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PLP

Summary: Perl in HTML pages
Name: perl-PLP
Version: 3.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PLP/

Source: http://www.cpan.org/authors/id/S/SH/SHIAR/PLP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
PLP is yet another Perl embedder, primarily for HTML documents. Unlike
with other Perl embedders, there is no need to learn a meta-syntax or
object model: one can just use the normal Perl constructs. PLP runs
under mod_perl for speeds comparable to those of PHP, but can also be
run as a CGI script.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/PLP.pm
%{perl_vendorlib}/PLP

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.22-1
- Updated to version 3.22.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.19-2.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 3.19-2
- Fixed the source url.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 3.19-1
- Updated to release 3.19.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.18-1
- Initial package.
