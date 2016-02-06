Name:      halvm-yum-repo
Version:   %{?fedora}
Release:   2%{?dist}
Summary:   HaLVM Yum Repository Configuration

Group:     System Environment/Base
License:   BSD
URL:       http://halvm.org
Source0:   halvm.repo
Source1:   RPM-GPG-KEY-HaLVM
BuildArch: noarch
Requires:  system-release >= %{version}

%description
The HaLVM Yum repository contains debugging-friendly versions of the Xen
hypervisor as well as binary builds of the HaLVM. Source RPMs are available
for those interested. Other tools of interest may be added as they become
available.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
install -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg 
install -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%{__install} -Dp -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -Dp -m644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%files
%{_sysconfdir}/pki/rpm-gpg/%{basename:%{SOURCE1}}
%config %{_sysconfdir}/yum.repos.d/%{basename:%{SOURCE0}}



%changelog

