# $Id$

# Authority: dries
# Upstream: Sam Tregar <sam$tregar,com>

%define real_name Class-XPath
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Adds xpath matching to object trees
Name: perl-Class-XPath
Version: 1.4
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-XPath/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/Class-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module adds XPath-style matching to your object trees. This means
that you can find nodes using an XPath-esque query with "match()" from
anywhere in the tree. Also, the "xpath()" method returns a unqique path
to a given node which can be used as an identifier.

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
%{perl_vendorlib}/Class/XPath.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
