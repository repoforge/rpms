# $Id$
# Authority: dag
# Upstream: Ron Isaacson <isaacson$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Tree
%define real_version 1

Summary: Perl module to format a simple tree of strings into a textual tree graph
Name: perl-Text-Tree
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Tree/

Source: http://www.cpan.org/modules/by-module/Text/Text-Tree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Text-Tree is a Perl module to format a simple tree of strings
into a textual tree graph.

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
%doc CHANGELOG MANIFEST README
%doc %{_mandir}/man3/Text::Tree.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Tree.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
