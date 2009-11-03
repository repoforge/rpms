# $Id$
# Authority: dries

Summary: Convert C++ code to latex
Name: cpp2latex
Version: 2.3
Release: 2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.arnoldarts.de/cpp2latex.html

Source: http://www.arnoldarts.de/cpp2latex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Cpp2latex can convert C++ code listings to a file you can input in a
LaTeX-document.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/cpp2latex

%changelog
* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 2.3-2
- Rebuild for fixing group on older packages (<fc3).

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Initial package.
