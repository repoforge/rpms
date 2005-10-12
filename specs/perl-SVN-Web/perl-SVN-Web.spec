# $Id$
# Authority: dries
# Upstream: clkao$clkao,org

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Web

Summary: Subversion repository web frontend
Name: perl-SVN-Web
Version: 0.38
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Web/

Source: http://www.cpan.org/modules/by-module/OurNet/CLKAO/SVN-Web-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Template-Toolkit, perl-YAML, perl-XML-RSS, perl-Text-Diff
BuildRequires: perl-Locale-Maketext-Simple, subversion-perl

%description
SVN::Web is a subversion repository web frontend.

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
%doc CHANGES README TODO
%doc %{_mandir}/man3/*
%{_bindir}/svnweb-install
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Web.pm
%{perl_vendorlib}/SVN/Web/

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Initial package.
