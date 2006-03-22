# $Id$
# Authority: dries
# Upstream: Christopher Nehren <apeiron$comcast,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Pluggable-Ordered

Summary: Call module plugins in a specified order
Name: perl-Module-Pluggable-Ordered
Version: 1.4
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Pluggable-Ordered/

Source: http://search.cpan.org/CPAN/authors/id/A/AP/APEIRON/Module-Pluggable-Ordered-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module behaves exactly the same as "Module::Pluggable", supporting
all of its options, but also mixes in the "call_plugins" method to your
class. "call_plugins" acts a little like "Class::Trigger"; it takes the
name of a method, and some parameters.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Pluggable/Ordered.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
