# $Id$

# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define real_name Pod-POM
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: POD Object Model
Name: perl-Pod-POM
Version: 0.17
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-POM/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABW/Pod-POM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements a parser to convert Pod documents into a simple
object model form known hereafter as the Pod Object Model.	The object
model is generated as a hierarchical tree of nodes, each of which
represents a different element of the original document.  The tree can
be walked manually and the nodes examined, printed or otherwise
manipulated.  In addition, Pod::POM supports and provides view objects
which can automatically traverse the tree, or section thereof, and
generate an output representation in one form or another.

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
%doc %{_mandir}/man1/*
%{_bindir}/podlint
%{_bindir}/pom2
%{perl_vendorlib}/Pod/POM.pm
%{perl_vendorlib}/Pod/POM
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
