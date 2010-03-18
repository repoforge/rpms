# $Id$
# Authority: shuff
# Upstream: Khemir Nadim ibn Hamouda <nadim$khemir,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-TreeDumper

Summary: Improved replacement for Data::Dumper
Name: perl-%{real_name}
Version: 0.37
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-TreeDumper/

Source: http://search.cpan.org/CPAN/authors/id/N/NK/NKH/Data-TreeDumper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Check::ISA)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Devel::Size) >= 0.58
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(Term::Size) >= 0.2
BuildRequires: perl(Text::Wrap) >= 2001.0929
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Data::Dumper and other modules do a great job of dumping data structures. Their
output, however, often takes more brain power to understand than the data
itself. When dumping large amounts of data, the output can be overwhelming and
it can be difficult to see the relationship between each piece of the dumped
data.

Data::TreeDumper also dumps data in a tree-like fashion but hopefully in a
format more easily understood.

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
%doc Changes MANIFEST README Todo
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/*

%changelog
* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 0.37-1
- Initial version.
