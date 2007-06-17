# $Id$
# Authority: dries
# Upstream: Christopher H. Laco <claco$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-NetBlogger

Summary: Post and retrieve blog entries
Name: perl-Catalyst-Model-NetBlogger
Version: 0.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-NetBlogger/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLACO/Catalyst-Model-NetBlogger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl >= 5.8.0

%description
This model class uses Net::Blogger to post and retrieve blog entries to
various web log engines XMLRPC API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Model/
%{perl_vendorlib}/Catalyst/Model/NetBlogger.pm
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Helper/
%dir %{perl_vendorlib}/Catalyst/Helper/Model/
%{perl_vendorlib}/Catalyst/Helper/Model/NetBlogger.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.

