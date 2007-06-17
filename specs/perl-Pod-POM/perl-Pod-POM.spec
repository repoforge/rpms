# $Id$
# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-POM

Summary: POD Object Model
Name: perl-Pod-POM
Version: 0.17
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-POM/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-POM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/podlint
%{_bindir}/pom2
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/POM.pm
%{perl_vendorlib}/Pod/POM/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
