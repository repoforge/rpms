# $Id$
# Authority: shuff
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,com>
# ExcludeDist: el3 el4

# el6 ships with perl-Devel-StackTrace-1.22, we need a later version
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)


%define real_name Plack

Summary: Perl Superglue for Web frameworks and servers (PSGI toolkit)
Name: perl-Plack
Version: 0.9979
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://plackperl.org/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1
BuildRequires: perl(Devel::StackTrace) >= 1.23
BuildRequires: perl(Devel::StackTrace::AsHTML) >= 0.11
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ShareDir) >= 1.00
BuildRequires: perl(Filesys::Notify::Simple)
BuildRequires: perl(HTTP::Body) >= 1.06
BuildRequires: perl(Hash::MultiValue) >= 0.05
BuildRequires: perl(LWP) >= 5.814
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::TCP) >= 0.11
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(URI) >= 1.36
BuildRequires: perl(parent)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Devel::StackTrace) >= 1.23
Requires: perl(Devel::StackTrace::AsHTML) >= 0.11
Requires: perl(File::ShareDir) >= 1.00
Requires: perl(Filesys::Notify::Simple)
Requires: perl(HTTP::Body) >= 1.06
Requires: perl(Hash::MultiValue) >= 0.05
Requires: perl(LWP) >= 5.814
Requires: perl(Pod::Usage)
Requires: perl(Test::TCP) >= 0.11
Requires: perl(Try::Tiny)
Requires: perl(URI) >= 1.36
Requires: perl(parent)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application frameworks.
Plack is like Ruby's Rack or Python's Paste for WSGI.

See PSGI for the PSGI specification and PSGI::FAQ to know what PSGI and Plack
are and why we need them.

%prep
%setup -n %{real_name}-%{version}

# damn it Module::Install
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.42.*/ && s/6\.42/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL --skipdeps INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%doc eg/dot-psgi/ benchmarks/
%{perl_vendorlib}/Plack.pm
%{perl_vendorlib}/Plack/*
%{perl_vendorlib}/HTTP/Message/*
%{perl_vendorlib}/HTTP/Server/*
%{perl_vendorlib}/auto/share/dist/Plack/
%{_bindir}/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Thu May 26 2011 Steve Huff <shuff@vecna.org> - 0.9979-1
- Updated to version 0.9979.

* Mon May 16 2011 Steve Huff <shuff@vecna.org> - 0.9978-1
- Initial package.
