# $Id$
# Authority: shuff
# Upstream: Matthias Miller <info$javascriptlint,com>

Summary:        Check JavaScript code for common mistakes
Name:           jsl
Version:        0.3.0
Release:        2%{?dist}
License:        MPLv1.1
Group:          Development/Tools
URL:            http://javascriptlint.com/

Source:         http://javascriptlint.com/download/jsl-%{version}-src.tar.gz
Patch0:         jsl-0.3.0-smash.patch
Patch1:         jsl-0.3.0-tests.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make

Provides: %{name} = %{version}
Provides: javascriptlint = %{version}

%description
With JavaScript Lint, you can check all your JavaScript source code for
common mistakes without actually running the script or opening the web page.

JavaScript Lint holds an advantage over competing lints because it is based
on the JavaScript engine for the Firefox browser. This provides a robust
framework that can not only check JavaScript syntax but also examine the
coding techniques used in the script and warn against questionable
practices.


%prep
%setup
%patch0 -p1 -b .smash
%patch1 -p1 -b .tests


%build
# Fix DOS-y EOL encoding and permissions
find . -type f |xargs sed -i 's/\r//' $FILES
find . -type f |xargs chmod 644 $FILES

# Dependencies dealt with poorly -- no _smp_mflags
%{__make} -C src -f Makefile.ref SHARED_LIBRARY= \
        OBJDIR=. JS_EDITLINE=1 XCFLAGS="%{optflags}" \
        OS_CFLAGS="-DXP_UNIX -DHAVE_VA_COPY -DVA_COPY=va_copy"


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_bindir}
%{__install} src/jsl $RPM_BUILD_ROOT%{_bindir}


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%check
cd tests
%{__perl} run_tests.pl ../src/jsl


%files
%defattr(-,root,root,-)
%{_bindir}/*


%changelog
* Wed Nov 18 2009 Steve Huff <shuff@vecna.org> - 0.3.0-2
- Initial package (ported from EPEL).

* Tue Apr 14 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.0-1
- Initial packaging
