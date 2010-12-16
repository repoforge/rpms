# $Id$
# Authority: shuff
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>
# ExcludeDist: el3 el4

### EL6 ships with perl-Devel-StackTrace-1.22-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-StackTrace-AsHTML

Summary: Displays stack trace in HTML
Name: perl-Devel-StackTrace-AsHTML
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-StackTrace-AsHTML/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)%{?!el5: >= 6.42}
BuildRequires: perl(Devel::StackTrace)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Devel::StackTrace)
Requires: perl(Filter::Util::Call)

### remove autoreq Perl dependencies
%filter_from_requires /^perl*/d
%filter_setup

%description
Devel::StackTrace::AsHTML adds as_html method to Devel::StackTrace which
displays the stack trace in beautiful HTML, with code snippet context and
function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical variables of
each stack frame.

%prep
%setup -n %{real_name}-%{version}

# damn it Module::Install
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.42.*/ && s/6\.\d+/6.30/' Makefile.PL}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Devel/StackTrace/
%{perl_vendorlib}/Devel/StackTrace/AsHTML.pm
# %{perl_vendorlib}/Devel/StackTrace/AsHTML/

%changelog
* Thu Dec 16 2010 Steve Huff <shuff@vecna.org> - 0.09-1
- Initial package.
