# $Id$
# Authority: dries
# Upstream: Christopher H. Laco <claco$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-SVN

Summary: Catalyst Model to browse Subversion repositories
Name: perl-Catalyst-Model-SVN
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-SVN/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLACO/Catalyst-Model-SVN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This model class uses the perl-subversion bindings to access a
Subversion repository and list items and view their contents. It is
currently only a read-only client but may expand to be a fill fledged
client at a later time.

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
%{perl_vendorlib}/Catalyst/Model/SVN.pm
%{perl_vendorlib}/Catalyst/Helper/Model/SVN.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
