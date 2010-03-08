# $Id$
# Authority: dries
# Upstream: Todd Rinaldo <toddr@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-MultiNode

Summary: Multi node unordered tree objects
Name: perl-Tree-MultiNode
Version: v1.0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-MultiNode/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Tree-MultiNode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build) >= 0.35
BuildRequires: perl(Test::More) >= 0.40

%filter_from_requires /^perl*/d
%filter_setup


%description
This is an implementation of a multi node tree.  The uniqueness of
keys is not enforced, nor is there enforcement of ordering of nodes.

Tree::MultiNode was created to aid in modeling heriarchical
relationships, like the relationships inherent in the records from
a RDBMS.  Where multi-to-multi relationships could produce multiple
child nodes with the same types or basic attributes.  Unique key
enforcement would be inappropriate in these cases (at least for me).

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
%{perl_vendorlib}/Tree/MultiNode.pm

%changelog
* Mon Mar  8 2010 Christoph Maser <cmr@financial.com> - v1.0.13-1
- Updated to version v1.0.13.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.10-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.10-1
- Initial package.
