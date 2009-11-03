# $Id$
# Authority: dries
# Upstream: Stephen McCamant <smcc$CSUA,Berkeley,EDU>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Graph

Summary: Perl compiler backend to produce graphs of OP trees
Name: perl-B-Graph
Version: 0.51
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Graph/

Source: http://www.cpan.org/modules/by-module/B/B-Graph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is a layer between the perl-internals-examining parts of
Malcolm Beattie's perl compiler (the B::* classes) and your favorite
graph layout tool (currently Dot and VGC are supported, but adding
others would be easy). It examines the internal structures that perl
builds to represent your code (OPs and SVs), and generates
specifications for multicolored boxes and arrows to represent them.

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
%{perl_vendorlib}/B/Graph.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Initial package.
