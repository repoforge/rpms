# $Id$
# Authority: dag

Summary: Strips Tex and LaTex commands from a file
Name: detex
Version: 2.8
Release: 1%{?dist}
License: BSD
Group: Applications/Text
URL: http://www.cs.purdue.edu/homes/trinkle/detex/ 

Source: http://www.cs.purdue.edu/homes/trinkle/detex/detex-%{version}.tar
Patch0: detex-2.8-mallocandtroff.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex
BuildRequires: groff

%description
DeTeX is a filter program that removes the LaTeX (or TeX)
control sequences from the input so that the real content can be
passed to a spell or diction checker

%prep
%setup
%patch

%build
%{__make} detex man-page prefix="%{_prefix}" CFLAGS="%{optflags} -DNO_MALLOC_DECL"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 detex %{buildroot}%{_bindir}/detex
%{__install} -Dp -m0644 detex.1 %{buildroot}%{_mandir}/man1/detex.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/detex.1*
%{_bindir}/detex

%changelog
* Tue Apr 21 2009 Hoffmann Geerd-Dietger <didi@ribalba.de> - 2.8-1
- Initial package.
