# $Id$
# Authority: dag

Summary: Utility for converting windows pfm font metric files into afm metrics
Name: pfm2afm
Version: 1.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/File
URL: http://pegasus.rutgers.edu/~elflord/font_howto/pfm2afm.tgz

Source: http://pegasus.rutgers.edu/~elflord/font_howto/pfm2afm.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
pfm2afm is a utility for converting windows pfm font metric files
into afm metrics that can be used for Linux. This is based on the
original version available at CTAN, and includes modificationsxi
from Rod Smith to make it compile under Linux.

%prep
%setup -c

%build
%{__cc} %{optflags} -o pfm2afm pfm2afm.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pfm2afm %{buildroot}%{_bindir}/pfm2afm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/pfm2afm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
