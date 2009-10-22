# $Id$
# Authority: shuff
# Upstream: Nate Wiger <nate$wiger,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-FormBuilder

Summary: Easily generate and process stateful forms
Name: perl-%{real_name}
Version: 3.0501
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-FormBuilder/

Source: http://search.cpan.org/CPAN/authors/id/N/NW/NWIGER/CGI-FormBuilder-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(CGI)
BuildRequires: perl(CGI::FastTemplate) >= 1.09
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Template) >= 2.06
BuildRequires: perl(Template) >= 2.08
BuildRequires: perl(Text::Template) >= 1.43
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(CGI)
Requires: perl(CGI::FastTemplate) >= 1.09
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(HTML::Template) >= 2.06
Requires: perl(Template) >= 2.08
Requires: perl(Text::Template) >= 1.43

### specify Perl dependencies by hand
%filter_from_requires /^perl.*/d
%filter_setup

%description
I hate generating and processing forms. Hate it, hate it, hate it, hate it. My
forms almost always end up looking the same, and almost always end up doing the
same thing. Unfortunately, there haven't really been any tools out there that
streamline the process. Many modules simply substitute Perl for HTML code:

    # The manual way
    print qq(<input name="email" type="text" size="20">);

    # The module way
    print input(-name => 'email', -type => 'text', -size => '20');

The problem is, that doesn't really gain you anything - you still have just as
much code. Modules like CGI.pm are great for decoding parameters, but not for
generating and processing whole forms.

The goal of CGI::FormBuilder (FormBuilder) is to provide an easy way for you to
generate and process entire CGI form-based applications. Its main features are:

Field Abstraction

    Viewing fields as entities (instead of just params), where the HTML
    representation, CGI values, validation, and so on are properties of each 
    field.

DWIMmery

    Lots of built-in "intelligence" (such as automatic field typing), giving
    you about a 4:1 ratio of the code it generates versus what you have to 
    write.

Built-in Validation

    Full-blown regex validation for fields, even including JavaScript code
    generation.  

Template Support

    Pluggable support for external template engines, such as HTML::Template,
    Text::Template, Template Toolkit, and CGI::FastTemplate.

Plus, the native HTML generated is valid XHTML 1.0 Transitional.

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
find %{buildroot} -name '*.orig' -exec %{__rm} -f {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST README 
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/*

%changelog
* Thu Oct 22 2009 Steve Huff <shuff@vecna.org> - 3.0501-1
- Initial package.
